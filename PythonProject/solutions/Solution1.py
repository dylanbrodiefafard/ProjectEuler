from solutions.BaseSolution import BaseSolution


class Solution1(BaseSolution):
    NUMBER = 1
    VERIFIED_ANSWER = 233168

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        sum_of_multiples_of_3_or_5 = 0
        for n in range(1000):
            if n % 3 == 0 or n % 5 == 0:
                sum_of_multiples_of_3_or_5 += n
        return sum_of_multiples_of_3_or_5


if __name__ == '__main__':
    Solution1().print_answer()
