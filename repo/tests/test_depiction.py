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
                "min_ios": "7.0",
                "description": "<p>Fade animation across keyboard typing.</p>",
            }

            with mock.patch.object(rendering, "depictions_dir", depictions_dir), mock.patch.object(
                rendering, "sileo_depictions_dir", sileo_depictions_dir
            ):
                generated_count = rendering.generate_depictions([entry])

            self.assertEqual(generated_count, 1)
            self.assertTrue((depictions_dir / "smoothkb.html").exists())
            self.assertTrue((sileo_depictions_dir / "smoothkb.json").exists())

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


if __name__ == "__main__":
    unittest.main()