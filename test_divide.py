import unittest
from divide import divide

class TestDivide(unittest.TestCase): #функция с набором проверок
    def test_divide_positive(self): #примеры с проверкой на деление с положит рез
        self.assertEqual(divide(6, 2), 3.0)
        self.assertEqual(divide(25, 4), 6.25)

    def test_divide_negative(self): #примеры с проверкой на деление с отрицат рез
        self.assertEqual(divide(-20, 2), -10.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)

    def test_divide_by_zero(self): #проверка на дление на 0
        with self.assertRaises(ZeroDivisionError):
            divide(21, 0)

    def test_divide_float(self): #проверка на деление дробей
        self.assertEqual(divide(10.5, 2.5), 4.2)


if __name__ == '__main__':
    unittest.main()
