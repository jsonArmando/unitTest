import unittest


class DummyClass:
    x = 5


class AssertIsNot(unittest.TestCase):
    def test_positive(self):
        firstValue = DummyClass()
        secondValue = DummyClass()
        message = "First value and second value evaluated to same object !"
        self.assertIsNot(firstValue, secondValue, message)


if __name__ == '__main__':
    unittest.main()
