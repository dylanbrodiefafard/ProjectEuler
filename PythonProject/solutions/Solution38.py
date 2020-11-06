from itertools import permutations

from solutions.SolutionBase import SolutionBase


class Solution38(SolutionBase):
    NUMBER = 38
    VERIFIED_ANSWER = 932718654

    def run_tests(self, test_case):
        test_case.assertTupleEqual((192, (1, 2, 3)), self.factor_pandigital('192384576'))
        test_case.assertTupleEqual((9, (1, 2, 3, 4, 5)), self.factor_pandigital('918273645'))

    @staticmethod
    def factor_pandigital(digits: str):
        for i in range(1, len(digits)):
            multiplicand, leftover_digits = int(digits[:i]), digits[i:]
            product = multiplicand * 2
            next_product_digits = ''
            while leftover_digits:
                # Make sure our next product to check is at least at long as our target product
                num_to_take = max(len(str(product)) - len(next_product_digits), 1)
                # But we can't take more digits than we have left
                i = min(num_to_take, len(leftover_digits))
                next_product_digits, leftover_digits = next_product_digits + leftover_digits[:i], leftover_digits[i:]
                if product == (next_product := int(next_product_digits)):
                    if not leftover_digits:
                        return multiplicand, tuple(range(1, 1 + next_product // multiplicand))
                    product += multiplicand
                    next_product_digits = ''
                elif next_product > product:
                    break

    def get_answer(self):
        for perm in permutations('987654321'):
            digits = ''.join(perm)
            if self.factor_pandigital(digits) is not None:
                return int(digits)


if __name__ == '__main__':
    Solution38().print_answer()
