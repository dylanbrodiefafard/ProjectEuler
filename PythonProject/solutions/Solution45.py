from solutions.SolutionBase import SolutionBase
from util.sequences import pentagonal_numbers, hexagonal_numbers, triangular_numbers


class Solution45(SolutionBase):
    NUMBER = 45
    VERIFIED_ANSWER = 1533776805

    def run_tests(self, test_case):
        gen = self.triangular_pentagonal_hexagonal()
        test_case.assertTupleEqual((0, 0, 0, 0), next(gen))
        test_case.assertTupleEqual((1, 1, 1, 1), next(gen))

    def get_answer(self):
        for t_i, p_i, h_i, n in self.triangular_pentagonal_hexagonal():
            if t_i > 285:
                return n

    @staticmethod
    def triangular_pentagonal_hexagonal():
        pentagonal_generator = enumerate(pentagonal_numbers())
        hexagonal_generator = enumerate(hexagonal_numbers())
        p_i, p = next(pentagonal_generator)
        h_i, h = next(hexagonal_generator)
        for t_i, t in enumerate(triangular_numbers()):
            while t > p:
                p_i, p = next(pentagonal_generator)
            while t > h:
                h_i, h = next(hexagonal_generator)
            if t == p == h:
                yield t_i, p_i, h_i, t


if __name__ == '__main__':
    Solution45().print_answer()
