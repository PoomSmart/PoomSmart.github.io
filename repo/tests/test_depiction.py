import tempfile
import unittest
from pathlib import Path
from unittest import mock

import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
GEN_DIR = REPO_ROOT / "gen"
sys.path.insert(0, str(GEN_DIR))

import depiction


class DepictionTests(unittest.TestCase):
    def test_validate_entry_rejects_missing_keys(self):
        with self.assertRaises(ValueError):
            depiction.validate_entry({"file": "broken"})

    def test_collect_screenshots_missing_directory_returns_empty_list(self):
        with mock.patch.object(depiction, "warn") as warn:
            screenshots = depiction.collect_screenshots("missing-screenshots")

        self.assertEqual(screenshots, [])
        warn.assert_called_once()

    def test_collect_screenshots_missing_directory_raises_in_strict_mode(self):
        with self.assertRaises(depiction.DepictionAssetError):
            depiction.collect_screenshots("missing-screenshots", strict=True)

    def test_collect_screenshots_is_sorted(self):
        screenshots = depiction.collect_screenshots("igetmorechoices")
        self.assertEqual(
            [shot["accessibilityText"] for shot in screenshots],
            sorted(shot["accessibilityText"] for shot in screenshots),
        )

    def test_load_inline_source_code_raises_in_strict_mode(self):
        with self.assertRaises(depiction.DepictionAssetError):
            depiction.load_inline_source_code("missing-source", "Missing Source", strict=True)

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

            with mock.patch.object(depiction, "depictions_dir", depictions_dir), mock.patch.object(
                depiction, "sileo_depictions_dir", sileo_depictions_dir
            ):
                generated_count = depiction.generate_depictions([entry])

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

        with self.assertRaises(depiction.DepictionAssetError):
            depiction.generate_depictions([entry], strict=True)


if __name__ == "__main__":
    unittest.main()