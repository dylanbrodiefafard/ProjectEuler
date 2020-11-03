from collections import namedtuple

from solutions.SolutionBase import SolutionBase


class Solution14(SolutionBase):
    NUMBER = 14
    VERIFIED_ANSWER = 837799

    def run_tests(self, test_case):
        chain_lengths = {1: 1}
        test_case.assertEqual(10, self.chain_length(13, chain_lengths))
        test_case.assertDictEqual({13: 10, 40: 9, 20: 8, 10: 7, 5: 6, 16: 5, 8: 4, 4: 3, 2: 2, 1: 1}, chain_lengths)

    @staticmethod
    def chain_length(n: int, known_chain_lengths: dict):
        chain = [n]
        while n != 1:
            if n & 1:
                n = (3 * n + 1)
            else:
                n //= 2
            if n in known_chain_lengths:
                break
            chain.append(n)
        chain_length = len(chain) + known_chain_lengths.get(n, 0)
        for i, x in enumerate(chain):
            known_chain_lengths[x] = chain_length - i
        return chain_length

    def get_answer(self):
        Answer = namedtuple('Answer', ['n', 'chain_length'])
        answer = Answer(None, 0)
        chain_lengths = {13: 10, 40: 9, 20: 8, 10: 7, 5: 6, 16: 5, 8: 4, 4: 3, 2: 2, 1: 1}
        get_chain_length = self.chain_length
        for n in range(13, 1000000, 1):
            if n in chain_lengths:
                continue
            if (chain_length := get_chain_length(n, chain_lengths)) > answer.chain_length:
                answer = Answer(n, chain_length)
        return answer.n


if __name__ == '__main__':
    Solution14().print_answer()
