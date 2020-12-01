import unittest
import calc

class TestDay1(unittest.TestCase):
    def test_add(self):
        year = 2020
        result = calc.add(10, 2010)
        self.assertEqual(result, year)

        result = calc.add(220, 1800)
        self.assertEqual(result, year)

        result = calc.add(420, 800)
        self.assertNotEqual(result,year)

    def test_multiply(self):
        result = calc.multiply(10, 200)
        self.assertEqual(result, 2000)

        result = calc.multiply(50, 10)
        self.assertEqual(result, 500)
        self.assertNotEqual(result, 501)


if __name__ == '__main__':
    unittest.main()