import unittest

from exercises.fibonacci import fibonacci


class FibonacciTestCases(unittest.TestCase):

    def test_is_valid_fib(self):
        fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
        for index, item in enumerate(fib_list):
            self.assertEqual(fibonacci(index), item)

    def test_is_not_valid_fib(self):
        for i in range(10, 20):
            self.assertNotEqual(fibonacci(i), i)


if __name__ == "__main__":
    unittest.main()
