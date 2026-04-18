# PoomSmart.github.io

This repository contains both the public website and the build inputs for the package repository published at `https://poomsmart.github.io/repo/`.

## Structure

- `index.html`, `emojiport.html`, `assets/`, `misc/`, `web/`: static site content served by GitHub Pages.
- `repo/gen/`: Python source for generating depiction HTML and Sileo JSON.
- `repo/templates/`: Jinja templates used by the generator.
- `repo/depictions/`, `repo/sileodepictions/`: generated outputs committed to the repository.
- `repo/debs/`, `repo/Packages*`, `repo/Release`: APT-style repository artifacts.

## Requirements

- Python 3.11+
- `uv` for dependency management
- For full package index rebuilds on macOS: `brew install dpkg zstd lz4`

## Build Depictions

Install Python dependencies:

```bash
uv sync --directory repo
```

Generate depiction HTML and Sileo JSON:

```bash
uv run --directory repo python main.py
```

Run the smoke tests:

```bash
uv run --directory repo python -m unittest discover -s tests
```

For stricter asset validation when working on a specific entry, import the generator and call `generate_depictions(..., strict=True)` so missing screenshot folders or missing inline source files fail immediately instead of being treated as warnings.

You can also invoke the script directly:

```bash
uv run --directory repo python gen/depiction.py
```

## Rebuild Repository Metadata

After generating depictions, rebuild the package indexes and compressed variants:

```bash
cd repo
./import.sh
```

`import.sh` regenerates depictions, rebuilds `Packages`, and emits the compressed package lists used by clients.

## Notes

- Generated depictions are committed intentionally because they are published directly from this repository.
- The GitHub Actions workflow validates that depiction generation stays reproducible and that committed outputs are up to date.