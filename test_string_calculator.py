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
        self.assertEqual(self.sc.add("995"), 995,
                         "Must return single digit number")

    def test_return_sum_of_given_string_number(self):
        self.assertEqual(self.sc.add("1,2,3"), 6,
                         "Must return sum of given input string")
        self.assertEqual(self.sc.add("1,2,3,4,5,6,7,8,9,10"), 55,
                         "Must return the sum of the given string")

    def test_return_sum_of_given_string_with_alphabet(self):
        self.assertEqual(self.sc.add("1,a,2,b,3,c"), 12,
                         "Must return sum also including alphabet")

    def test_throws_exception_if_string_number_contains_negative_number(self):
        self.assertRaises(ValueError, self.sc.add, "1,-2,-4,3")

    def test_throws_exception_with_list_of_negative_number(self):
        self.assertRaises(ValueError, self.sc.add, "1,-2,-3,-4")
