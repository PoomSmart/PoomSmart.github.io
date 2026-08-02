import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { transformSync } from "@babel/core";
import * as acorn from "acorn";
import { minify } from "terser";

const SITE_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

const JS_FILES = [
  ["misc/iosver.js", "misc/iosver.min.js"],
  ["assets/emojiport.js", "assets/emojiport.min.js"],
];

function validateEs5(code, outputRel) {
  try {
    acorn.parse(code, { ecmaVersion: 5, sourceType: "script" });
  } catch (error) {
    throw new Error(`ES5 validation failed for ${outputRel}: ${error.message}`);
  }
}

async function buildJs(sourceRel, outputRel) {
  const sourcePath = path.join(SITE_ROOT, sourceRel);
  const outputPath = path.join(SITE_ROOT, outputRel);
  const source = readFileSync(sourcePath, "utf8");

  const transpiled = transformSync(source, {
    babelrc: false,
    configFile: false,
    comments: false,
    presets: [
      [
        "@babel/preset-env",
        {
          targets: {
            ios: "5",
          },
          bugfixes: true,
        },
      ],
    ],
  });

  if (!transpiled.code) {
    throw new Error(`Transpilation produced no output for ${sourceRel}`);
  }

  const minified = await minify(transpiled.code, {
    ecma: 5,
    compress: true,
    mangle: true,
    format: {
      ecma: 5,
    },
  });

  if (!minified.code) {
    throw new Error(`Minification produced no output for ${sourceRel}`);
  }

  const output = minified.code.endsWith("\n") ? minified.code : `${minified.code}\n`;
  validateEs5(output, outputRel);
  writeFileSync(outputPath, output, "utf8");
  console.log(`Built ${sourceRel} -> ${outputRel}`);
}

for (const [sourceRel, outputRel] of JS_FILES) {
  await buildJs(sourceRel, outputRel);
}
