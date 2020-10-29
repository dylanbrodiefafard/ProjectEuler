from solutions.BaseSolution import BaseSolution


class Solution13(BaseSolution):
    NUMBER = 13
    VERIFIED_ANSWER = 5537376230

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        numbers = (
            int(line.strip())
            for line in self.get_lines_from_data_file_in_archive('p013.zip', 'p013_numbers.txt')
        )
        return int(str(sum(numbers))[:10])


if __name__ == '__main__':
    Solution13().print_answer()
