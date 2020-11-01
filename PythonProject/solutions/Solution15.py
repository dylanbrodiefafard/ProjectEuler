from solutions.SolutionBase import SolutionBase
from util.integers import factorial


class Solution15(SolutionBase):
    NUMBER = 15
    VERIFIED_ANSWER = 137846528820

    def run_tests(self, test_case):
        test_case.assertEqual(6, self.num_lattice_paths(2, 2))

    @staticmethod
    def num_lattice_paths(n, m):
        return int(factorial(m + n) / (factorial(m) * factorial(n)))

    def get_answer(self):
        return self.num_lattice_paths(20, 20)


if __name__ == '__main__':
    Solution15().print_answer()
