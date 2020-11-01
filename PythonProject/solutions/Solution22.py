from solutions.SolutionBase import SolutionBase


class Solution22(SolutionBase):
    NUMBER = 22
    VERIFIED_ANSWER = 871198282
    LETTERS_TO_NUMBERS = letters = {
        letter: i + 1 for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    }

    def run_tests(self, test_case):
        test_case.assertEqual(49714, self.word_score('COLIN', 938))

    @staticmethod
    def word_score(word, word_position):
        return sum(map(Solution22.LETTERS_TO_NUMBERS.get, word)) * word_position

    def get_answer(self):
        total_scores = 0
        lines = self.get_lines_from_data_file_in_archive('p022.zip', 'p022_names.txt')
        words = sorted(word.replace('"', '') for word in lines[0].split(','))
        for i, word in enumerate(words):
            total_scores += self.word_score(word, i + 1)
        return total_scores


if __name__ == '__main__':
    Solution22().print_answer()
