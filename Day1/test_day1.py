import unittest
import day1

class TestDay1(unittest.TestCase):
    def test_multiply(self):
        result = day1.multiply(10, 20)
        self.assertEqual(result, 2020)


if __name__ == '__main__':
    unittest.main()