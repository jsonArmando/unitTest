import unittest


class Tests(unittest.TestCase):
    one = 0
    two = 0
    result = True

    def setUp(self) -> None:
        self.one = 10
        self.two = 4
        if self.two * self.one == 2:
            self.result = False

    def sub(self):
        self.assertEqual(self.one + self.two, 4)
        self.assertTrue(self.result())

    def rest(self):
        self.assertTrue(self.one - self.two == 0)
        self.assertTrue(self.result())



if __name__ == '__main__':
    unittest.main()
