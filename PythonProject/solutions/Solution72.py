from solutions.SolutionBase import SolutionBase
from util.integers import totient_sum


class Solution72(SolutionBase):
    NUMBER = 72
    VERIFIED_ANSWER = 303963552391

    def run_tests(self, test_case):
        test_case.assertEqual(21, self.get_num_reduced_proper_fractions_with_denominator_up_to(8))

    @staticmethod
    def get_num_reduced_proper_fractions_with_denominator_up_to(max_denominator):
        # Don't count the 1/1 fraction (totient(1) = 1)
        return totient_sum(max_denominator) - 1

    def get_answer(self):
        return self.get_num_reduced_proper_fractions_with_denominator_up_to(1000000)


if __name__ == '__main__':
    Solution72().print_answer()
