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
        self.assertEqual(self.sc.add("y,a,s,h"), 53,
                         "Must return sum also including alphabet")

    def test_throws_exception_if_string_number_contains_negative_number(self):
        self.assertRaises(ValueError, self.sc.add, "1,-2,-4,3")

    def test_throws_exception_with_list_of_negative_number(self):
        self.assertRaises(ValueError, self.sc.add, "1,-2,-3,-4")

    # optional

    # delimiter can be '\n' or ','
    def test_with_two_different_delimiter(self):
        self.assertEquals(self.sc.add("1,2,3\n4\n5\n6,7,8,9,10"),
                          55, "Must return sum with two different delimiter")

    # delimiter must be take from the string itself
    def test_with_defined_delimiter_in_string_number(self):
        self.assertEqual(self.sc.add("//;;\n1;;2;;3;;4;;5;;6;;7;;8;;9;;10"), 55,
                         "Must return sum with defined delimiter")

    # sum of all elements which are on odd indicies.
    def test_if_zero_in_input_string_sum_element_of_odd_indices(self):
        self.assertEqual(self.sc.add("0//;;\n12;;33;;44;;a;;b;;c"), 58)

    # sum of all elements which are on even indicies.
    def test_if_one_in_input_string_sum_elements_of_even_indices(self):
        self.assertEqual(self.sc.add("1//;\n12;33;44;a;b;c"), 37)
        self.assertEqual(self.sc.add("1//;;\n12;;b;;c"), 2)
