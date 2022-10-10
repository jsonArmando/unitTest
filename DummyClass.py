import unittest


class DummyClass:
    x = 5


class TestMethods(unittest.TestCase):
    def test_positive(self):
        firstValue = None
        message = "Test value is not none."
        self.assertIsNone(firstValue, message)


if __name__ == '__main__':
    unittest.main()
