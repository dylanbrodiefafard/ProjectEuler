from solutions.SolutionBase import SolutionBase
from util.sequences import prime_numbers_up_to


class Solution49(SolutionBase):
    NUMBER = 49
    VERIFIED_ANSWER = 296962999629
    KNOWN_TERMS = (1487, 4817, 8147)

    def run_tests(self, test_case):
        test_case.assertIn(self.KNOWN_TERMS, set(self.prime_permutations()))

    @staticmethod
    def prime_permutations():
        four_digit_primes = {p for p in prime_numbers_up_to(9999) if p > 1000}
        for p1 in sorted(four_digit_primes):
            p2, p3 = p1 + 3330, p1 + 2 * 3330
            if p2 in four_digit_primes and p3 in four_digit_primes:
                p1_digits = set(str(p1))
                if p1_digits == set(str(p2)) and p1_digits == set(str(p3)):
                    yield p1, p2, p3

    def get_answer(self):
        for terms in self.prime_permutations():
            if terms == self.KNOWN_TERMS:
                continue
            return int(''.join(map(str, terms)))


if __name__ == '__main__':
    Solution49().print_answer()
