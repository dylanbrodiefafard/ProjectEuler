from solutions.SolutionBase import SolutionBase
from util.more_functools import prod


class Solution40(SolutionBase):
    NUMBER = 40
    VERIFIED_ANSWER = 210

    def run_tests(self, test_case):
        test_case.assertListEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 2, 0, 2, 1],
            [self.nth_digit_of_concatenated_positive_integers(n) for n in range(1, 34)]
        )
        expected_digit = int((''.join(map(str, range(1, 101))))[99])
        test_case.assertEqual(expected_digit, self.nth_digit_of_concatenated_positive_integers(100))
        expected_digit = int((''.join(map(str, range(1, 1001))))[999])
        test_case.assertEqual(expected_digit, self.nth_digit_of_concatenated_positive_integers(1000))
        expected_digit = int((''.join(map(str, range(1, 10001))))[9999])
        test_case.assertEqual(expected_digit, self.nth_digit_of_concatenated_positive_integers(10000))

    @staticmethod
    def nth_digit_of_concatenated_positive_integers(n: int):
        assert n > 0
        power_of_ten, num_digits, digit_index_within_number, number = 10, 2, 0, n
        while number > power_of_ten:
            # Update number and index within that number
            number -= ((number - power_of_ten) % num_digits) + ((number - power_of_ten) // num_digits)
            digit_index_within_number = n % num_digits
            # Increment our loop variables
            power_of_ten, num_digits, n = power_of_ten * 10, num_digits + 1, n - power_of_ten

        # The digit will be the index within the number
        return int(str(number)[digit_index_within_number])

    def get_answer(self):
        n_digits = (1, 10, 100, 1000, 10000, 100000, 1000000)
        return prod(map(self.nth_digit_of_concatenated_positive_integers, n_digits))


if __name__ == '__main__':
    Solution40().print_answer()
