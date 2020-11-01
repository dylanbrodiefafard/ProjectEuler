from itertools import permutations

from solutions.SolutionBase import SolutionBase
from util.primes import is_prime


class Solution41(SolutionBase):
    NUMBER = 41
    VERIFIED_ANSWER = 7652413

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        largest_pandigital_prime = 0
        digits = '1'
        for x in range(2, 10):
            digits += str(x)
            # it's at least a 4-digit so skip 2 and 3. 5,6,8,9 all add up to multiples of 3 so none of them will be prime
            if not (x == 4 or x == 7):
                continue
            for pandigital in permutations(digits):
                number = int(''.join(pandigital))
                if number > largest_pandigital_prime and is_prime(number):
                    largest_pandigital_prime = number

        assert largest_pandigital_prime != 0
        return largest_pandigital_prime


if __name__ == '__main__':
    Solution41().print_answer()
