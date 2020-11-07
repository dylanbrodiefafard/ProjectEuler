from solutions.SolutionBase import SolutionBase


class Solution48(SolutionBase):
    NUMBER = 48
    VERIFIED_ANSWER = 9110846700

    def run_tests(self, test_case):
        test_case.assertEqual('1317', self.last_n_digits_of_series(4, 10))
        test_case.assertEqual('0405071317', self.last_n_digits_of_series(10, 10))

    @staticmethod
    def last_n_digits_of_series(n: int, max_val: int):
        last_n_digits_sum = 0

        # Use modular exponentiation because we only care about some of the last digits.
        modulo_value = 10 ** n
        for m in range(1, max_val + 1):
            last_n_digits_sum += pow(m, m, modulo_value)

        # Make sure to zero pad the left because integers don't keep leading zeros.
        return (str(last_n_digits_sum)[-n:]).zfill(n)

    def get_answer(self):
        return int(self.last_n_digits_of_series(10, 1000))


if __name__ == '__main__':
    Solution48().print_answer()
