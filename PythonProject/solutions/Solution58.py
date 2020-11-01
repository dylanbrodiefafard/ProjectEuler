from solutions.BaseSolution import BaseSolution
from util.primes import is_prime
from util.sequences import spiral_diagonal


class P58(BaseSolution):
    NUMBER = 58
    VERIFIED_ANSWER = 26241

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        side_length = 3
        num_primes_along_diagonals = 0
        num_along_diagonals = 1
        values_along_diagonals_gen = spiral_diagonal()
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
