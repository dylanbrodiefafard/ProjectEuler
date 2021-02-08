from collections import deque

from solutions.SolutionBase import SolutionBase
from util.sequences import prime_numbers_up_to


class Solution35(SolutionBase):
    NUMBER = 35
    VERIFIED_ANSWER = 55

    def run_tests(self, test_case):
        test_case.assertEqual([2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97], self.circular_primes(100))

    @staticmethod
    def circular_primes(up_to: int):
        primes = set(prime_numbers_up_to(up_to))
        circular_primes = []
        while primes:
            circular_family = [prime := primes.pop()]
            for _ in range(len(digits := deque(str(prime))) - 1):
                digits.rotate(1)
                other_maybe_prime = int(''.join(digits))
                if prime == other_maybe_prime:
                    continue
                circular_family.append(other_maybe_prime)
                if other_maybe_prime not in primes:
                    break
            else:
                circular_primes.extend(circular_family)
                primes.difference_update(circular_family)
        circular_primes.sort()
        return circular_primes

    def get_answer(self):
        return len(self.circular_primes(1000000))


if __name__ == '__main__':
    Solution35().print_answer()
