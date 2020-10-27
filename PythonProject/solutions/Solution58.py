from itertools import islice

from solutions.BaseSolution import BaseSolution
from util.primes import is_prime


class P58(BaseSolution):
    NUMBER = 58
    VERIFIED_ANSWER = 26241

    def run_tests(self, test_case):
        test_case.assertListEqual(
            [3, 5, 7, 9],
            list(islice(self.values_along_diagonals(), 4))
        )
        test_case.assertListEqual(
            [3, 5, 7, 9, 13, 17, 21, 25],
            list(islice(self.values_along_diagonals(), 8))
        )
        test_case.assertListEqual(
            [3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49],
            list(islice(self.values_along_diagonals(), 12))
        )

    @staticmethod
    def values_along_diagonals():
        value = 3
        n = 1
        side_length = 3
        while True:
            yield value
            if n == 4:
                side_length += 2
                n = 1
            else:
                n += 1
            value += (side_length - 1)

    def get_answer(self):
        side_length = 3
        num_primes_along_diagonals = 0
        num_along_diagonals = 1
        values_along_diagonals_gen = self.values_along_diagonals()
        while True:
            for _ in range(4):
                if is_prime(next(values_along_diagonals_gen)):
                    num_primes_along_diagonals += 1
            num_along_diagonals += 4
            prime_ratio = num_primes_along_diagonals / num_along_diagonals
            if prime_ratio < 0.1:
                return side_length
            side_length += 2


if __name__ == '__main__':
    P58().print_answer()
