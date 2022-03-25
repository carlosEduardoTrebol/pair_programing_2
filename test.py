#CARLOS
import unittest
import main

class FibonacciShould(unittest.TestCase):

    def test_returns_i_if_number_1(self):
        number=1
        letter = main.Roman_Numbers().roman_number_transform_to_decimal(number)
        self.assertEqual(letter, "i")

    def test_returns_ii_if_number_2(self):
        number=2
        letter = main.Roman_Numbers().roman_number_transform_to_decimal(number)
        self.assertEqual(letter, "ii")
    def test_returns_iii_if_number_3(self):
        number=3
        letter = main.Roman_Numbers().roman_number_transform_to_decimal(number)
        self.assertEqual(letter, "iii")

