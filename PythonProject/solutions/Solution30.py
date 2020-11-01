from solutions.SolutionBase import SolutionBase


class Solution30(SolutionBase):
    NUMBER = 30
    VERIFIED_ANSWER = 443839

    def run_tests(self, test_case):
        test_case.assertEqual([1634, 8208, 9474], sorted(self.numbers_with_digital_sum_of_nth_powers(4)))
        test_case.assertEqual(19316, sum(self.numbers_with_digital_sum_of_nth_powers(4)))

    @staticmethod
    def numbers_with_digital_sum_of_nth_powers(n: int):
        limit = int(n * 9 ** n)
        digit_powers = {str(d): d ** n for d in range(10)}
        for m in range(10, limit):
            if sum(map(digit_powers.get, str(m))) == m:
                yield m

    def get_answer(self):
        return sum(self.numbers_with_digital_sum_of_nth_powers(5))


if __name__ == '__main__':
    Solution30().print_answer()
