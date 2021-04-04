from solutions.SolutionBase import SolutionBase


class Solution13(SolutionBase):
    NUMBER = 13
    VERIFIED_ANSWER = 5537376230

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        numbers = map(int, self.get_lines_from_data_file('p013_numbers.txt'))
        return int(str(sum(numbers))[:10])


if __name__ == '__main__':
    Solution13().print_answer()
