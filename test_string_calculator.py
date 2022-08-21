from distutils.core import setup
import unittest
from string_calculator import StringCalculator


class StringCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.sc = StringCalculator()

    def test_return_zero_if_string_is_empty(self):
        self.assertEqual(self.sc.add(""), 0, "Must return 0 for empty string")

    def test_return_number_if_string_has_one_number_only(self):
        self.assertEqual(self.sc.add("1"), 1,
                         "Must  return number passed in parameter")
        self.assertEqual(self.sc.add("15"), 15,
                         "Must  return number passed in parameter")

    def test_return_sum_of_given_string_number(self):
        self.assertEqual(self.sc.add("1,2,3"), 6,
                         "Must return sum of given input string")

    def test_return_sum_of_given_string_with_alphabet(self):
        self.assertEqual(self.sc.add("1,a,2,b,3,c"), 12,
                         "Must return sum also including alphabet")
