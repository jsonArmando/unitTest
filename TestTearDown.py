import unittest
from unittest import IsolatedAsyncioTestCase
import os


class TestTearDown(IsolatedAsyncioTestCase):
    def __init__(self):
        self.file = "file.txt"
        default_contents = "Jose, Armando"
        with open(self.file, "w") as f:
            f.write(default_contents)

    def empty_tank(self):
        os.remove(self.file)


class TestAdvancedFishTank(unittest.TestCase):
    def setUp(self):
        self.name = TestTearDown()

    def tearDown(self):
        self.name.empty_tank()

    def test_writes_file(self):
        with open(self.name.file) as f:
            contents = f.read()
        self.assertEqual(contents, "Jose, Armando")


if __name__ == "__main__":
    unittest.main()
