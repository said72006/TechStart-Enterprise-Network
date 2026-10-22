import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class NetworkProjectTests(unittest.TestCase):
    def test_deliverables_exist(self):
        design = ROOT / "TechStart_Enterprise_Network.pkt"
        report = ROOT / "TechStart_Final_Report.pdf"
        self.assertTrue(design.is_file())
        self.assertGreater(design.stat().st_size, 1000)
        self.assertTrue(report.is_file())
        self.assertEqual(report.read_bytes()[:4], b"%PDF")

    def test_documented_images_exist(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        paths = re.findall(r"!\[[^]]*\]\(([^)]+)\)", text)
        self.assertGreater(len(paths), 0)
        for image in paths:
            with self.subTest(image=image):
                self.assertTrue((ROOT / image).is_file(), image)

    def test_ftp_warning(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("FTP transmits credentials and data without encryption", text)


if __name__ == "__main__":
    unittest.main()
