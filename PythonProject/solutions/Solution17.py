from solutions.SolutionBase import SolutionBase


class Solution17(SolutionBase):
    NUMBER = 17
    VERIFIED_ANSWER = 21124
    NUM_LETTERS_BY_NUMBER = {
        0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7,
        17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8
    }

    def run_tests(self, test_case):
        test_case.assertEqual(19, self.num_letters_used_to_write_out(1, 5))

    @staticmethod
    def num_letters_used_to_write_out(min_val, max_val):
        assert 0 <= min_val < max_val <= 1000

        num_letters = 0
        for n in range(min_val, max_val + 1):
            digits = str(n)
            if n >= 1000:
                num_letters += Solution17.NUM_LETTERS_BY_NUMBER[1000]
                if n % 1000 != 0:
                    num_letters += 3  # add "and" to the number
            if 100 <= n < 1000:
                num_letters += Solution17.NUM_LETTERS_BY_NUMBER[100]
                if n % 100 != 0:
                    num_letters += 3  # add "and" to the number
            for i in range(len(digits), 0, -1):
                if i == 2:
                    if int(digits[-2:]) >= 20:
                        num_letters += Solution17.NUM_LETTERS_BY_NUMBER[int(digits[-2:-1]) * 10]
                    else:
                        num_letters += Solution17.NUM_LETTERS_BY_NUMBER[int(digits[-2:])]
                        break
                elif i == 1:
                    num_letters += Solution17.NUM_LETTERS_BY_NUMBER[int(digits[-i:])]
                else:
                    num_letters += Solution17.NUM_LETTERS_BY_NUMBER[int(digits[-i:-i+1])]
        return num_letters

    def get_answer(self):
        return self.num_letters_used_to_write_out(1, 1000)


if __name__ == '__main__':
    Solution17().print_answer()
