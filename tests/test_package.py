import unittest
from src.c950.package import Package
from src.c950.status import PackageStatus


class TestPackage(unittest.TestCase):

    def test_package(self):
        package = Package(1, "123 Main Street", "Salt Lake City", "UT", "84111", 10, "EOD", "Some note", PackageStatus.AT_HUB)
        self.assertEqual(package.package_id, 1)
        self.assertEqual(package.address, "123 Main Street")
        self.assertEqual(package.city, "Salt Lake City")
        self.assertEqual(package.state, "UT")
        self.assertEqual(package.zip_code, "84111")
        self.assertEqual(package.weight, 10)
        self.assertEqual(package.deadline, "EOD")
        self.assertEqual(package.note, "Some note")
        self.assertEqual(package.status, PackageStatus.AT_HUB)


if __name__ == '__main__':
    unittest.main()
