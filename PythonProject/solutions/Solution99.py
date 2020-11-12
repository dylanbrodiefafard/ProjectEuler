from collections import namedtuple
from math import log

from solutions.SolutionBase import SolutionBase
from util.integers import NEGATIVE_INFINITY


class Solution99(SolutionBase):
    NUMBER = 99
    VERIFIED_ANSWER = 709

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        Answer = namedtuple('Answer', ['line_no', 'value'])
        answer = Answer(-1, NEGATIVE_INFINITY)
        for line_i, line in enumerate(self.get_lines_from_data_file_in_archive('p099.zip', 'p099_base_exp.txt')):
            base, exponent = tuple(map(int, line.split(',')))
            value = log(base) * exponent
            if value > answer.value:
                answer = Answer(line_i + 1, value)
        return answer.line_no


if __name__ == '__main__':
    Solution99().print_answer()
