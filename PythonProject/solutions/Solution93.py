from collections import namedtuple
from itertools import permutations, product
from operator import mul, add, sub, truediv

from solutions.SolutionBase import SolutionBase


def eq1(a, b, c, d, op1, op2, op3):
    return op3(op2(op1(a, b), c), d)


def eq2(a, b, c, d, op1, op2, op3):
    return op2(op1(a, b), op3(c, d))


def eq3(a, b, c, d, op1, op2, op3):
    return op3(op1(a, op2(b, c)), d)


def eq4(a, b, c, d, op1, op2, op3):
    return op1(a, op3(op2(b, c), d))


def eq5(a, b, c, d, op1, op2, op3):
    return op1(a, op2(b, op3(c, d)))


class Solution93(SolutionBase):
    NUMBER = 93
    VERIFIED_ANSWER = 1258
    OPERATORS = (mul, add, truediv, sub)
    EQUATIONS = (eq1, eq2, eq3, eq4, eq5)

    def run_tests(self, test_case):
        test_case.assertEqual(28, self.num_consecutive_positive_integers({1, 2, 3, 4}))

    @staticmethod
    def num_consecutive_positive_integers(digits):
        values = set()
        for a, b, c, d in permutations(digits):
            for op1, op2, op3 in product(Solution93.OPERATORS, repeat=3):
                for eq in Solution93.EQUATIONS:
                    try:
                        values.add(eq(a, b, c, d, op1, op2, op3))
                    except ZeroDivisionError:
                        continue
        n = 1
        while n in values:
            n += 1
        return n - 1

    def get_answer(self):
        Answer = namedtuple('Answer', ['num_consecutive', 'digits'])
        answer = Answer(0, set())
        for a in range(1, 10):
            for b in range(a + 1, 10):
                for c in range(b + 1, 10):
                    for d in range(c + 1, 10):
                        digits = {a, b, c, d}
                        num_consecutive = self.num_consecutive_positive_integers(digits)
                        if num_consecutive > answer.num_consecutive:
                            answer = Answer(num_consecutive, digits)
        return int(''.join(map(str, sorted(answer.digits))))


if __name__ == '__main__':
    Solution93().print_answer()
