from solutions.SolutionBase import SolutionBase

DENOMINATIONS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


def to_roman(n: int) -> str:
    """
    Converts an integer to a minimal form roman numeral.
    See https://projecteuler.net/about=roman_numerals for more details on the form.
    :param n: The number to convert.
    :return: The minimal roman numeral form.
    """
    numeral = ''
    for current_numeral, current_value in DENOMINATIONS.items():
        num_divisible = n // current_value
        numeral += current_numeral * num_divisible
        n -= current_value * num_divisible
    return numeral


def from_roman(numerals: str) -> int:
    """
    Converts a roman numeral form (not necessarily minimal) of a number into an integer.
    :param numerals: The roman numeral to convert.
    :return: The integer value.
    """
    n = 0
    max_numeral_value = None
    for numeral in reversed(numerals):
        value = DENOMINATIONS[numeral]
        if max_numeral_value is None or value >= max_numeral_value:
            n += value
            max_numeral_value = value
        else:
            n -= value
    return n


class Solution89(SolutionBase):
    NUMBER = 89
    VERIFIED_ANSWER = 743

    def run_tests(self, test_case):
        test_case.assertEqual(49, from_roman('XXXXIIIIIIIII'))
        test_case.assertEqual(49, from_roman('XXXXVIIII'))
        test_case.assertEqual(49, from_roman('XXXXIX'))
        test_case.assertEqual(49, from_roman('XLIIIIIIIII'))
        test_case.assertEqual(49, from_roman('XLVIIII'))
        test_case.assertEqual(49, from_roman('XLIX'))
        test_case.assertEqual(49, from_roman('XLIX'))
        test_case.assertEqual(1606, from_roman('MCCCCCCVI'))
        test_case.assertEqual(1606, from_roman('MDCVI'))
        test_case.assertEqual('I', to_roman(1))
        test_case.assertEqual('II', to_roman(2))
        test_case.assertEqual('IV', to_roman(4))
        test_case.assertEqual('XVI', to_roman(16))
        test_case.assertEqual('XLIX', to_roman(49))
        test_case.assertEqual('MDCVI', to_roman(1606))

    def get_answer(self):
        numeral_length = minimal_numeral_length = 0
        for numeral in self.get_lines_from_data_file('p089_roman.txt'):
            numeral_length += len(numeral)
            minimal_numeral_length += len(to_roman(from_roman(numeral)))
        return numeral_length - minimal_numeral_length


if __name__ == '__main__':
    Solution89().print_answer()
