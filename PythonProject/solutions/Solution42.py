from solutions.SolutionBase import SolutionBase
from util.sequences import triangular


class Solution42(SolutionBase):
    NUMBER = 42
    VERIFIED_ANSWER = 162
    LETTERS_TO_NUMBERS = letters = {
        letter: i + 1 for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    }

    def __init__(self):
        self._triangle_numbers = set()
        self._triangular_generator = triangular()
        self._max_triangle_number = 0

    def run_tests(self, test_case):
        test_case.assertEqual(55, self.word_value('SKY'))
        test_case.assertTrue(self.is_triangular(55))

    @staticmethod
    def word_value(word):
        return sum(map(Solution42.LETTERS_TO_NUMBERS.get, word))

    def is_triangular(self, n):
        while n > self._max_triangle_number:
            self._triangle_numbers.add(t := next(self._triangular_generator))
            self._max_triangle_number = t
        return n in self._triangle_numbers

    def get_answer(self):
        num_triangular_words = 0
        lines = self.get_lines_from_data_file_in_archive('p042.zip', 'p042_words.txt')
        for word in lines[0].split(','):
            word = word.replace('"', '')
            if self.is_triangular(self.word_value(word)):
                num_triangular_words += 1
        return num_triangular_words


if __name__ == '__main__':
    Solution42().print_answer()
