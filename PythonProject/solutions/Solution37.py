from itertools import chain

from solutions.SolutionBase import SolutionBase
from util.integers import append_digits, prepend_digits
from util.primes import is_prime


class Solution37(SolutionBase):
    NUMBER = 37
    VERIFIED_ANSWER = 748317
    SINGLE_DIGIT_PRIMES = [2, 3, 5, 7]

    @staticmethod
    def is_truncatable_prime(number):
        if len(str(number)) <= 1:
            return False

        if not is_prime(number):
            return False

        digits = str(number)[:-1]
        while len(digits) > 0:
            if not is_prime(int(digits)):
                return False
            digits = digits[:-1]

        digits = str(number)[1:]
        while len(digits) > 0:
            if not is_prime(int(digits)):
                return False
            digits = digits[1:]

        return True

    def run_tests(self, test_case):
        test_case.assertTrue(self.is_truncatable_prime(3797))
        test_case.assertFalse(self.is_truncatable_prime(2))
        test_case.assertFalse(self.is_truncatable_prime(3))
        test_case.assertFalse(self.is_truncatable_prime(5))
        test_case.assertFalse(self.is_truncatable_prime(7))

    def get_next_candidates(self, number, seen_numbers):
        appended_candidates = (append_digits(number, d) for d in self.SINGLE_DIGIT_PRIMES)
        prepended_candidates = (prepend_digits(d, number) for d in range(1, 10))
        return {
            candidate
            for candidate in chain(appended_candidates, prepended_candidates)
            if candidate not in seen_numbers and is_prime(candidate)
        }

    def get_answer(self):
        # numbers must start and end with single digits primes.
        truncatable_primes = set()
        candidates = set()
        seen_numbers = set()
        for n in self.SINGLE_DIGIT_PRIMES:
            candidates.update(self.get_next_candidates(n, seen_numbers))

        while candidates:
            candidate = candidates.pop()
            if self.is_truncatable_prime(candidate):
                truncatable_primes.add(candidate)
                if len(truncatable_primes) == 11:
                    break
            seen_numbers.add(candidate)
            candidates.update(self.get_next_candidates(candidate, seen_numbers))

        assert len(truncatable_primes) == 11, \
            'Expected to find 11 truncatable primes, but found {}'.format(len(truncatable_primes))

        return sum(truncatable_primes)


if __name__ == '__main__':
    Solution37().print_answer()
