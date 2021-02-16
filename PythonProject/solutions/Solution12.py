from solutions.SolutionBase import SolutionBase
from util.integers import multiplicative_partitions, num_divisors
from util.more_functools import prod
from util.sequences import triangular_numbers, prime_numbers


class Solution12(SolutionBase):
    NUMBER = 12
    VERIFIED_ANSWER = 76576500

    def run_tests(self, test_case):
        test_case.assertEqual(1, self.first_triangle_number_over_divisors(0))
        test_case.assertEqual(3, self.first_triangle_number_over_divisors(1))
        test_case.assertEqual(6, self.first_triangle_number_over_divisors(2))
        test_case.assertEqual(6, self.first_triangle_number_over_divisors(3))
        test_case.assertEqual(28, self.first_triangle_number_over_divisors(5))

    @staticmethod
    def smallest_number_with_exactly_n_divisors(n):
        assert n > 0
        if n == 1 or n == 2:
            return n
        return min(
            prod(prime ** (divisor - 1) for prime, divisor in zip(prime_numbers(), partition))
            for partition in multiplicative_partitions(n)
        )

    @staticmethod
    def triangular_index_floor(n):
        # Finds the index of the closest triangular number to n (rounded down)
        return int(0.5 * (-1 + ((1 + 8 * n) ** 0.5)))

    @staticmethod
    def first_triangle_number_over_divisors(n):
        if n == 0:
            return 1
        minimum_number = Solution12.smallest_number_with_exactly_n_divisors(n)
        index_of_minimum_triangular_number = Solution12.triangular_index_floor(minimum_number)
        for number in triangular_numbers(index_of_minimum_triangular_number):
            if num_divisors(number) > n:
                return number

    def get_answer(self):
        return self.first_triangle_number_over_divisors(500)


if __name__ == '__main__':
    Solution12().print_answer()
