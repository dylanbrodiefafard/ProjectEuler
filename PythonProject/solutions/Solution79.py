from functools import cmp_to_key

from solutions.SolutionBase import SolutionBase


class Solution79(SolutionBase):
    NUMBER = 79
    VERIFIED_ANSWER = '73162890'

    def run_tests(self, test_case):
        test_case.assertEqual('1', self.get_minimal_passcode(['1']))
        test_case.assertEqual('12', self.get_minimal_passcode(['1', '2']))
        test_case.assertEqual('123', self.get_minimal_passcode(['12', '23']))
        test_case.assertEqual('1235', self.get_minimal_passcode(['12', '23', '13', '35']))
        test_case.assertEqual('01235', self.get_minimal_passcode(['012', '23', '13', '35']))
        test_case.assertEqual('12345', self.get_minimal_passcode(['12', '34', '15']))
        test_case.assertEqual('12345', self.get_minimal_passcode(['12', '14', '13', '15', '34']))

    @staticmethod
    def get_minimal_passcode(partial_passcodes):
        prev_digits = {}
        for partial_passcode in partial_passcodes:
            for i, digit in enumerate(partial_passcode):
                prev = prev_digits.setdefault(digit, set())
                if i > 0:
                    prev.add(partial_passcode[i - 1])

        def compare_partially_ordered_digits(a, b):
            pre_a = prev_digits[a]
            pre_b = prev_digits[b]
            if a in pre_b and b not in pre_a:
                return -1
            if b in pre_a and a not in pre_b:
                return 1
            return 0

        sorted_digits = sorted(prev_digits.keys(), key=cmp_to_key(compare_partially_ordered_digits))
        return ''.join(sorted_digits)

    def get_answer(self):
        partial_passcodes = self.get_lines_from_data_file('p079_keylog.txt')
        return self.get_minimal_passcode(partial_passcodes)


if __name__ == '__main__':
    Solution79().print_answer()
