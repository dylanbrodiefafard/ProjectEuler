from solutions.BaseSolution import BaseSolution
from util.primes import primes, is_prime


class P46(BaseSolution):
    NUMBER = 46
    VERIFIED_ANSWER = 5777

    def __init__(self):
        self._primes = []
        self._primes_generator = primes()

    def run_tests(self, test_case):
        test_case.assertTupleEqual((7, 1), self.get_coefficients(9))
        test_case.assertTupleEqual((7, 2), self.get_coefficients(15))
        test_case.assertTupleEqual((3, 3), self.get_coefficients(21))
        test_case.assertTupleEqual((7, 3), self.get_coefficients(25))
        test_case.assertTupleEqual((19, 2), self.get_coefficients(27))
        test_case.assertTupleEqual((31, 1), self.get_coefficients(33))

    def get_answer(self):
        n = 35
        while True:
            if not is_prime(n) and self.get_coefficients(n) is None:
                return n
            n += 2

    def primes_generator(self, max_prime):
        yield from self._primes
        for prime in self._primes_generator:
            self._primes.append(prime)
            if prime > max_prime:
                return
            yield prime

    def get_coefficients(self, n):
        for a in self.primes_generator(n - 2):
            for b in range(1, int(n ** .5) + 1):
                if a + 2 * (b ** 2) == n:
                    return a, b


if __name__ == '__main__':
    P46().print_answer()
