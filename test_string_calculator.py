from distutils.core import setup
import unittest
from string_calculator import StringCalculator


class StringCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.sc = StringCalculator()

    def test_return_zero_if_string_is_empty(self):
        self.assertEqual(self.sc.add(""), 0, "Must return 0 for empty string")
