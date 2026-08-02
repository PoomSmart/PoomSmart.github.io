import tempfile
import unittest
from pathlib import Path
from unittest import mock

import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from gen import app, data_loader, depiction, rendering


class DepictionTests(unittest.TestCase):
    def test_validate_entry_rejects_missing_keys(self):
        with self.assertRaisesRegex(data_loader.DepictionSchemaError, "required property"):
            data_loader.validate_entry({"file": "broken"})

    def test_validate_entry_rejects_unknown_keys(self):
        with self.assertRaisesRegex(data_loader.DepictionSchemaError, "Additional properties"):
            data_loader.validate_entry(
                {
                    "file": "broken",
                    "title": "Broken",
                    "description": "<p>Broken</p>",
                    "unexpected": True,
                }
            )

    def test_validate_entry_accepts_object_changelog(self):
        data_loader.validate_entry(
            {
                "file": "example",
                "title": "Example",
                "description": "<p>Example</p>",
                "changes": [
                    {
                        "version": "1.0.0",
                        "details": ["Initial release"],
                    }
                ],
            }
        )

    def test_parse_ios_range(self):
        open_ended = data_loader.parse_ios_range("[11.0,)")
        self.assertEqual(open_ended.min, "11.0")
        self.assertIsNone(open_ended.max)
        self.assertEqual(open_ended.label(), "Compatible with iOS 11.0 +")

        closed = data_loader.parse_ios_range("[8.0, 18.0]")
        self.assertEqual((closed.min, closed.max, closed.max_exclusive, closed.strict), ("8.0", "18.0", False, False))
        self.assertEqual(closed.label(), "Compatible with iOS 8.0 to 18.0")

        exclusive = data_loader.parse_ios_range("[8.0, 18.0)")
        self.assertTrue(exclusive.max_exclusive)
        self.assertEqual(exclusive.label(), "Compatible with iOS 8.0 to 17.x")

        self.assertEqual(
            data_loader.parse_ios_range("[14.0, 17.0)").label(),
            "Compatible with iOS 14.0 to 16.x",
        )

        self.assertEqual(
            data_loader.parse_ios_range("[14.0, 15.0)").label(),
            "Compatible with iOS 14.x",
        )

        strict = data_loader.parse_ios_range("[12.0, 17.0]!")
        self.assertTrue(strict.strict)
        self.assertFalse(strict.max_exclusive)

        exclusive_strict = data_loader.parse_ios_range("[14.0, 15.0)!")
        self.assertTrue(exclusive_strict.max_exclusive)
        self.assertTrue(exclusive_strict.strict)

    def test_parse_ios_range_rejects_strict_without_max(self):
        with self.assertRaisesRegex(data_loader.DepictionSchemaError, "upper bound"):
            data_loader.parse_ios_range("[11.0,)!")

    def test_validate_entry_accepts_ios_range(self):
        data_loader.validate_entry(
            {
                "file": "example",
                "title": "Example",
                "ios": "[9.0, 14.8.1]!",
                "description": "<p>Example</p>",
            }
        )

    def test_validate_entry_rejects_legacy_min_ios(self):
        with self.assertRaisesRegex(data_loader.DepictionSchemaError, "Additional properties"):
            data_loader.validate_entry(
                {
                    "file": "example",
                    "title": "Example",
                    "min_ios": "11.0",
                    "description": "<p>Example</p>",
                }
            )

    def test_load_category_uses_json_data(self):
        youtube_entries = data_loader.load_category("youtube")
        self.assertTrue(any(entry["file"] == "ytuhd" for entry in youtube_entries))

    def test_validate_all_categories_accepts_current_repo_data(self):
        data_loader.validate_all_categories()

    def test_legacy_category_module_uses_json_loader(self):
        self.assertEqual(app.app, data_loader.load_category("app"))

    def test_collect_screenshots_missing_directory_returns_empty_list(self):
        with mock.patch.object(rendering, "warn") as warn:
            screenshots = rendering.collect_screenshots("missing-screenshots")

        self.assertEqual(screenshots, [])
        warn.assert_called_once()

    def test_normalize_markup_removes_inter_tag_whitespace(self):
        markup = "  <p>First</p>            <p>Second</p><br/>            <p>Third</p>  "
        self.assertEqual(rendering.normalize_markup(markup), "<p>First</p><p>Second</p><br/><p>Third</p>")

    def test_collect_screenshots_missing_directory_raises_in_strict_mode(self):
        with self.assertRaises(rendering.DepictionAssetError):
            rendering.collect_screenshots("missing-screenshots", strict=True)

    def test_collect_screenshots_is_sorted(self):
        screenshots = rendering.collect_screenshots("igetmorechoices")
        self.assertEqual(
            [shot["accessibilityText"] for shot in screenshots],
            sorted(shot["accessibilityText"] for shot in screenshots),
        )

    def test_load_inline_source_code_raises_in_strict_mode(self):
        with self.assertRaises(rendering.DepictionAssetError):
            rendering.load_inline_source_code("missing-source", "Missing Source", strict=True)

    def test_generate_depictions_writes_expected_outputs(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            depictions_dir = tmp_path / "depictions"
            sileo_depictions_dir = tmp_path / "sileodepictions"
            depictions_dir.mkdir()
            sileo_depictions_dir.mkdir()

            entry = {
                "file": "smoothkb",
                "title": "SmoothKB",
                "ios": "[7.0,)",
                "description": "<p>Fade animation across keyboard typing.</p>",
            }

            with mock.patch.object(rendering, "depictions_dir", depictions_dir), mock.patch.object(
                rendering, "sileo_depictions_dir", sileo_depictions_dir
            ):
                generated_count = rendering.generate_depictions([entry])

            self.assertEqual(generated_count, 1)
            self.assertTrue((depictions_dir / "smoothkb.html").exists())
            self.assertTrue((sileo_depictions_dir / "smoothkb.json").exists())

    def test_generate_depictions_uses_executor_for_multiple_entries(self):
        class FakeExecutor:
            map_called = False
            received_max_workers = None

            def __init__(self, max_workers):
                FakeExecutor.received_max_workers = max_workers

            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc, tb):
                return False

            def map(self, func, iterable):
                FakeExecutor.map_called = True
                return [func(item) for item in iterable]

        entries = [
            {
                "file": "smoothkb",
                "title": "SmoothKB",
                "description": "<p>One</p>",
            },
            {
                "file": "recordpause",
                "title": "RecordPause",
                "description": "<p>Two</p>",
            },
        ]

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            depictions_dir = tmp_path / "depictions"
            sileo_depictions_dir = tmp_path / "sileodepictions"
            depictions_dir.mkdir()
            sileo_depictions_dir.mkdir()

            with mock.patch.object(rendering, "depictions_dir", depictions_dir), mock.patch.object(
                rendering, "sileo_depictions_dir", sileo_depictions_dir
            ), mock.patch.object(rendering, "ThreadPoolExecutor", FakeExecutor), mock.patch.object(
                rendering, "_max_workers", return_value=2
            ):
                generated_count = rendering.generate_depictions(entries)

        self.assertEqual(generated_count, 2)
        self.assertTrue(FakeExecutor.map_called)
        self.assertEqual(FakeExecutor.received_max_workers, 2)

    def test_generate_depictions_raises_for_missing_screenshots_in_strict_mode(self):
        entry = {
            "file": "missing-screenshots",
            "title": "Missing Screenshots",
            "description": "<p>Example</p>",
            "screenshots": True,
        }

        with self.assertRaises(rendering.DepictionAssetError):
            rendering.generate_depictions([entry], strict=True)

    def test_main_uses_loaded_tweaks(self):
        with mock.patch.object(depiction, "load_all_tweaks", return_value=[]), mock.patch.object(
            depiction, "generate_depictions", return_value=0
        ) as generate_depictions:
            depiction.main()

        generate_depictions.assert_called_once_with([], strict=False)

    def test_minify_assets_minifies_css(self):
        import minify_assets

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            assets_dir = tmp_path / "assets"
            assets_dir.mkdir()
            (assets_dir / "misc.css").write_text(".foo { color: red; }\n", encoding="utf-8")
            (assets_dir / "site.css").write_text(".bar { color: blue; }\n", encoding="utf-8")
            (assets_dir / "emojiport.css").write_text(".baz { color: green; }\n", encoding="utf-8")

            with mock.patch.object(minify_assets, "SITE_ROOT", tmp_path), mock.patch.object(
                minify_assets, "build_js"
            ):
                minify_assets.main()

            self.assertEqual((assets_dir / "misc.min.css").read_text(encoding="utf-8"), ".foo{color:red}\n")
            self.assertEqual((assets_dir / "site.min.css").read_text(encoding="utf-8"), ".bar{color:blue}\n")
            self.assertEqual((assets_dir / "emojiport.min.css").read_text(encoding="utf-8"), ".baz{color:green}\n")


if __name__ == "__main__":
    unittest.main()