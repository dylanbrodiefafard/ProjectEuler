from collections import namedtuple

from solutions.SolutionBase import SolutionBase
from util.integers import POSITIVE_INFINITY


class Solution85(SolutionBase):
    NUMBER = 85
    VERIFIED_ANSWER = 2772
    TARGET_NUM_RECTANGLES = 2000000

    def run_tests(self, test_case):
        test_case.assertEqual(18, self.num_rectangles(3, 2))

    @staticmethod
    def num_rectangles(n: int, m: int) -> int:
        return m * (m + 1) * n * (n + 1) // 4

    @staticmethod
    def max_width(target: int) -> int:
        # find maximum width by squaring until exceeding target
        n, num_rectangles = 1, 1
        while num_rectangles < target:
            n += 1
            num_rectangles = Solution85.num_rectangles(n, n)
        return n

    @staticmethod
    def max_length(target: int) -> int:
        # find maximum length by increasing one dimension
        n, num_rectangles = 1, 1
        while num_rectangles < target:
            n += 1
            num_rectangles = Solution85.num_rectangles(n, 1)
        return n

    def get_answer(self):
        target = Solution85.TARGET_NUM_RECTANGLES
        Answer = namedtuple('Answer', ['num_rectangles', 'diff', 'length', 'width'])
        answer = Answer(0, POSITIVE_INFINITY, 0, 0)
        max_width, max_length = self.max_width(target), self.max_length(target)
        for length in range(1, max_length + 1):
            for width in range(1, max_width + 1):
                num_rectangles = self.num_rectangles(length, width)
                diff = abs(num_rectangles - target)
                if diff < answer.diff:
                    answer = Answer(num_rectangles, diff, length, width)
                elif num_rectangles > answer.num_rectangles:
                    break
        return answer.length * answer.width


if __name__ == '__main__':
    Solution85().print_answer()
