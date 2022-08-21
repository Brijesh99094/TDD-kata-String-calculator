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
