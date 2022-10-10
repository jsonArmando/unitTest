import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('jose'.upper(), 'Jose')

    def test_isupper(self):
        self.assertTrue('JOSE'.isupper())
        self.assertFalse('Jose'.isupper())


if __name__ == '__main__':
    unittest.main()
