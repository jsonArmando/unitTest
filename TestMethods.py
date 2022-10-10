import unittest


class TestMethods(unittest.TestCase):
    def test_positive(self):
        firstValue = "geeks"
        message = "Test value is  none."
        self.assertIsNotNone(firstValue, message)


if __name__ == '__main__':
    unittest.main()
