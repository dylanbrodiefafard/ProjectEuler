from solutions.SolutionBase import SolutionBase
from util.sequences import prime_numbers


class Solution46(SolutionBase):
    NUMBER = 46
    VERIFIED_ANSWER = 5777

    def run_tests(self, test_case):
        test_case.assertTupleEqual((7, 1), self.get_coefficients(9, {2, 3, 5, 7}))
        test_case.assertTupleEqual((7, 2), self.get_coefficients(15, {2, 3, 5, 7, 11}))
        test_case.assertTupleEqual((3, 3), self.get_coefficients(21, {2, 3, 5, 7, 11, 13, 17, 19}))
        test_case.assertTupleEqual((7, 3), self.get_coefficients(25, {2, 3, 5, 7, 11, 13, 17, 19, 23}))
        test_case.assertTupleEqual((19, 2), self.get_coefficients(27, {2, 3, 5, 7, 11, 13, 17, 19, 23}))
        test_case.assertTupleEqual((31, 1), self.get_coefficients(33, {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}))

    def get_answer(self):
        primes_generator = prime_numbers()
        primes_so_far = [next(primes_generator)]
        get_coefficients = self.get_coefficients
        max_prime = max(primes_so_far)
        n = 35
        while True:
            while max_prime < n:
                primes_so_far.append(max_prime := next(primes_generator))
            if n != max_prime and get_coefficients(n, primes_so_far) is None:
                # Odd composite that doesn't fit the equation.
                return n
            n += 2

    @staticmethod
    def get_coefficients(n, candidates):
        max_b = int(n ** .5) + 1
        for a in candidates:
            for b in range(1, max_b):
                if a + 2 * (b ** 2) == n:
                    return a, b


if __name__ == '__main__':
    Solution46().print_answer()
