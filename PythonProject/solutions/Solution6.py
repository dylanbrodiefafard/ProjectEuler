from solutions.BaseSolution import BaseSolution


class Solution6(BaseSolution):
    NUMBER = 6
    VERIFIED_ANSWER = 25164150

    def run_tests(self, test_case):
        test_case.assertEqual(2640, self.get_difference(1, 10))

    @staticmethod
    def get_difference(min_val, max_val):
        sum_squares = 0
        square_sums = 0

        for n in range(min_val, max_val + 1):
            sum_squares += n * n
            square_sums += n

        return (square_sums * square_sums) - sum_squares

    def get_answer(self):
        return self.get_difference(1, 100)


if __name__ == '__main__':
    Solution6().print_answer()
