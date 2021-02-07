from solutions.SolutionBase import SolutionBase


class Solution97(SolutionBase):
    NUMBER = 97
    VERIFIED_ANSWER = '8739992577'

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        # Use modular exponentiation because we only care about some of the last digits.
        num_digits = 10
        last_digits_of_large_prime = 28433 * pow(2, 7830457, 10 ** num_digits) + 1
        return (str(last_digits_of_large_prime)[-num_digits:]).zfill(num_digits)


if __name__ == '__main__':
    Solution97().print_answer()
