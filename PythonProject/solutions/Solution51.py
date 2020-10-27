from collections import defaultdict

from solutions.BaseSolution import BaseSolution
from util.primes import primes, is_prime


class P51(BaseSolution):
    NUMBER = 51
    VERIFIED_ANSWER = 121313
    VALID_PRIME_ENDING_DIGITS = [1, 2, 3, 5, 7, 9]

    def __init__(self):
        self._max_prime_value_families = {}

    def run_tests(self, test_case):
        test_case.assertEqual(6, self.max_prime_value_family(13))
        test_case.assertEqual(6, self.max_prime_value_family(23))
        test_case.assertEqual(6, self.max_prime_value_family(43))
        test_case.assertEqual(6, self.max_prime_value_family(53))
        test_case.assertEqual(6, self.max_prime_value_family(73))
        test_case.assertEqual(6, self.max_prime_value_family(83))
        test_case.assertEqual(7, self.max_prime_value_family(56003))
        test_case.assertEqual(7, self.max_prime_value_family(56113))
        test_case.assertEqual(7, self.max_prime_value_family(56333))
        test_case.assertEqual(7, self.max_prime_value_family(56443))
        test_case.assertEqual(7, self.max_prime_value_family(56663))
        test_case.assertEqual(7, self.max_prime_value_family(56773))
        test_case.assertEqual(7, self.max_prime_value_family(56993))

    def max_prime_value_family(self, prime):
        if prime in self._max_prime_value_families:
            return len(self._max_prime_value_families[prime])

        digits = str(prime)
        num_digits = len(digits)
        max_prime_value_family = {prime}

        indexes_by_digit = defaultdict(set)
        for i, digit in enumerate(digits):
            indexes_by_digit[digit].add(i)

        for replacement_indexes in indexes_by_digit.values():
            if (num_digits - 1) in replacement_indexes:
                replacement_digits = self.VALID_PRIME_ENDING_DIGITS
            else:
                min_replacement_digit = 1 if 0 in replacement_indexes else 0
                replacement_digits = range(min_replacement_digit, 10)
            prime_value_family = set()
            for replacement_digit in replacement_digits:
                new_digits = list(digits)
                for index in replacement_indexes:
                    new_digits[index] = str(replacement_digit)
                new_digits = ''.join(new_digits)
                new_number = int(new_digits)
                if is_prime(new_number):
                    prime_value_family.add(new_number)
            if len(prime_value_family) > len(max_prime_value_family):
                max_prime_value_family = prime_value_family
        for p in max_prime_value_family:
            self._max_prime_value_families[p] = max_prime_value_family
        return len(self._max_prime_value_families[prime])

    def get_answer(self):
        self._max_prime_value_families.clear()
        for p in primes():
            if self.max_prime_value_family(p) == 8:
                return p


if __name__ == '__main__':
    P51().print_answer()
