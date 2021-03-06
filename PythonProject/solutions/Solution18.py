from collections import defaultdict

from solutions.SolutionBase import SolutionBase
from util.integers import NEGATIVE_INFINITY


class Solution18(SolutionBase):
    NUMBER = 18
    VERIFIED_ANSWER = 1074
    SMALLER_TRIANGLE = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3],
    ]
    LARGER_TRIANGLE = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]

    def run_tests(self, test_case):
        test_case.assertEqual(23, self.maximum_top_to_bottom_total(self.SMALLER_TRIANGLE))

    @staticmethod
    def maximum_top_to_bottom_total(triangle):
        max_of_children = defaultdict(lambda: NEGATIVE_INFINITY)
        # Propagate the maximum backwards.
        for row_i, row in reversed(list(enumerate(triangle))):
            for col_i, val in reversed(list(enumerate(row))):
                max_value_of_children = max(max_of_children[(row_i + 1, col_i)], max_of_children[(row_i + 1, col_i + 1)])
                if max_value_of_children is not NEGATIVE_INFINITY:
                    val += max_value_of_children
                max_of_children[(row_i, col_i)] = val
        return max_of_children[(0, 0)]

    def get_answer(self):
        return self.maximum_top_to_bottom_total(self.LARGER_TRIANGLE)


if __name__ == '__main__':
    Solution18().print_answer()
