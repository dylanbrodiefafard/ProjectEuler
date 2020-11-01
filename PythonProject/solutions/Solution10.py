from solutions.SolutionBase import SolutionBase
from util.primes import primes_up_to


class Solution10(SolutionBase):
    NUMBER = 10
    VERIFIED_ANSWER = 142913828922

    def run_tests(self, test_case):
        test_case.assertEqual(17, self.sum_of_primes_below(10))

    @staticmethod
    def sum_of_primes_below(n):
        return sum(primes_up_to(n - 1))

    def get_answer(self):
        return self.sum_of_primes_below(2000000)


if __name__ == '__main__':
    Solution10().print_answer()
