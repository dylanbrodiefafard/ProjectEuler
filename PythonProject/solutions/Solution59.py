from collections import namedtuple
from itertools import product

from solutions.SolutionBase import SolutionBase

ASCII_LETTERS = set(range(65, 91)) | set(range(97, 123))
ASCII_SPACE = 32


class Solution59(SolutionBase):
    NUMBER = 59
    VERIFIED_ANSWER = 129448

    def run_tests(self, test_case):
        message = """Seances occur only in darkened rooms, where the ghostly visitors can be seen dimly at best. If \
we turn up the lights a little, so we have a chance to see what's going on, the spirits vanish. They're shy, \
we're told, and some of us believe it. In twentieth-century parapsychology laboratories, there is the \
"observer effect": those described as gifted psychics find that their powers diminish markedly whenever \
sceptics arrive, and disappear altogether in the presence of a conjuror as skilled as James Randi. What they \
need is darkness and gullibility."""
        password = 'foo'
        encrypted_ascii_message = list(self.cyclical_xor(self.to_ascii(message), self.to_ascii(password)))
        ascii_password = self.get_cyclical_xor_password(encrypted_ascii_message, len(password))
        ascii_decrypted_message = self.cyclical_xor(encrypted_ascii_message, ascii_password)
        test_case.assertEqual(password, self.to_string(ascii_password))
        test_case.assertEqual(message, self.to_string(ascii_decrypted_message))

    @staticmethod
    def to_ascii(message):
        return list(map(ord, message))

    @staticmethod
    def to_string(ascii_codes):
        return ''.join(map(chr, ascii_codes))

    @staticmethod
    def cyclical_xor(ascii_message, ascii_password):
        password_length = len(ascii_password)
        for i, ascii_character in enumerate(ascii_message):
            yield ascii_character ^ ascii_password[i % password_length]

    @staticmethod
    def get_english_score(ascii_message):
        num_letters = num_spaces = word_length = num_characters = 0
        for character in ascii_message:
            num_characters += 1
            if character in ASCII_LETTERS:
                num_letters += 1
                word_length += 1
            elif character == ASCII_SPACE:
                num_spaces += 1
                word_length = 0
            else:
                word_length += 1
            if word_length > 25:
                return 0

        if num_characters == 0:
            return 0

        return (num_letters + num_spaces) / num_characters

    @staticmethod
    def get_cyclical_xor_password(ascii_message, password_length):
        Answer = namedtuple('Answer', ['score', 'password'])
        answer = Answer(0, None)

        for ascii_password in product(range(97, 123), repeat=password_length):
            score = Solution59.get_english_score(Solution59.cyclical_xor(ascii_message, ascii_password))
            if score > 0 and score > answer.score:
                answer = Answer(score, ascii_password)

        if answer.score == 0:
            raise ValueError('No password found')

        return answer.password

    def get_answer(self):
        text = self.get_lines_from_data_file('p059_cipher.txt')[0]
        ascii_message = list(map(int, text.split(',')))
        ascii_password = self.get_cyclical_xor_password(ascii_message, 3)
        decrypted_ascii = self.cyclical_xor(ascii_message, ascii_password)
        return sum(decrypted_ascii)


if __name__ == '__main__':
    Solution59().print_answer()
