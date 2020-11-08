from solutions.Solution18 import Solution18
from solutions.SolutionBase import SolutionBase


class Solution67(SolutionBase):
    NUMBER = 67
    VERIFIED_ANSWER = 7273

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        triangle = []
        for line in self.get_lines_from_data_file_in_archive('p067.zip', 'p067_triangle.txt'):
            triangle.append(list(map(int, line.split(' '))))
        return Solution18.maximum_top_to_bottom_total(triangle)


if __name__ == '__main__':
    Solution67().print_answer()
