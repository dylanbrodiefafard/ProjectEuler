from unittest import TestCase

from util.integers import *


class IntegersTest(TestCase):

    def test_prepend_digit(self):
        self.assertEqual(21, prepend_digits(2, 1))
        self.assertEqual(211, prepend_digits(2, 11))
        self.assertEqual(11, prepend_digits(0, 11))
        self.assertEqual(10, prepend_digits(1, 0))
        self.assertEqual(-11, prepend_digits(1, -1))
        self.assertEqual(-1100, prepend_digits(1, -100))
        self.assertEqual(909123, prepend_digits(90, 9123))
        self.assertEqual(123456, prepend_digits(123, 456))
        self.assertEqual(-123456, prepend_digits(123, -456))

    def test_append_digit(self):
        self.assertEqual(21, append_digits(2, 1))
        self.assertEqual(211, append_digits(2, 11))
        self.assertEqual(11, append_digits(0, 11))
        self.assertEqual(10, append_digits(1, 0))
        self.assertEqual(-11, append_digits(-1, 1))
        self.assertEqual(-1100, append_digits(-1, 100))
        self.assertEqual(909123, append_digits(90, 9123))
        self.assertEqual(123456, append_digits(123, 456))
        self.assertEqual(-123456, append_digits(-123, 456))

    def test_is_paldindrome(self):
        self.assertTrue(is_paldindrome(313))
        self.assertTrue(is_paldindrome(101))
        self.assertTrue(is_paldindrome(11))
        self.assertTrue(is_paldindrome(3))
        self.assertTrue(is_paldindrome(1000009000001))
        self.assertFalse(is_paldindrome(1000009100001))
        self.assertFalse(is_paldindrome(13))
        self.assertFalse(is_paldindrome(1011))
        self.assertFalse(is_paldindrome(9000091))

    def test_digital_sum(self):
        self.assertEqual(1, digital_sum(1))
        self.assertEqual(2, digital_sum(11))
        self.assertEqual(1, digital_sum(100))
        self.assertEqual(15, digital_sum(12345))
        self.assertEqual(15, digital_sum(123450))
        self.assertEqual(15, digital_sum(123405))
        self.assertEqual(15, digital_sum(102345))
