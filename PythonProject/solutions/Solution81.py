from collections import defaultdict

from solutions.SolutionBase import SolutionBase
from util.integers import POSITIVE_INFINITY


class Solution81(SolutionBase):
    NUMBER = 81
    VERIFIED_ANSWER = 427337
    SMALL_MATRIX = [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]

    def run_tests(self, test_case):
        test_case.assertEqual(2427, self.minimal_path_sum(self.SMALL_MATRIX))

    @staticmethod
    def minimal_path_sum(matrix):
        # Propagate minimum of children backwards.
        min_of_children = defaultdict(lambda: POSITIVE_INFINITY)
        for row_i, row in reversed(list(enumerate(matrix))):
            for col_i, val in reversed(list(enumerate(row))):
                min_value_of_children = min(min_of_children[(row_i, col_i + 1)], min_of_children[(row_i + 1, col_i)])
                if min_value_of_children is not POSITIVE_INFINITY:
                    val += min_value_of_children
                min_of_children[(row_i, col_i)] = val
        return min_of_children.get((0, 0))

    @staticmethod
    def matrix_from_lines(lines):
        return [list(map(int, line.split(','))) for line in lines]

    def get_answer(self):
        matrix = self.matrix_from_lines(self.get_lines_from_data_file('p081_matrix.txt'))
        return self.minimal_path_sum(matrix)


if __name__ == '__main__':
    Solution81().print_answer()
