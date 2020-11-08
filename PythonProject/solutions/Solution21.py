from solutions.SolutionBase import SolutionBase
from util.integers import aliquot_sum


class Solution21(SolutionBase):
    NUMBER = 21
    VERIFIED_ANSWER = 31626

    def run_tests(self, test_case):
        test_case.assertEqual(284, aliquot_sum(220))
        test_case.assertEqual(220, aliquot_sum(284))

    def get_answer(self):
        sum_amicable_numbers = 0
        numbers = list(range(2, 10000))
        while numbers:
            n = numbers.pop(0)
            sum_of_proper_factors = aliquot_sum(n)
            if n != sum_of_proper_factors and n == aliquot_sum(sum_of_proper_factors):
                numbers.remove(sum_of_proper_factors)
                sum_amicable_numbers += n + sum_of_proper_factors
        return sum_amicable_numbers


if __name__ == '__main__':
    Solution21().print_answer()
