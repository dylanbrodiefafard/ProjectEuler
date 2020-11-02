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
        chain_length = 1
        chain = [n]
        x = n
        while x != 1:
            is_odd = x & 1
            if is_odd:
                # 3 * x + 1 is always even, so we can go ahead twice when x is odd.
                x = (3 * x + 1) // 2
            else:
                x //= 2
            if x in known_chain_lengths:
                chain_length += known_chain_lengths[x]
                break
            if is_odd:
                # We skipped 2 steps when x was odd, so count them both here.
                chain_length += 2
                chain.extend((2 * x, x))
            else:
                chain_length += 1
                chain.append(x)
        # Record all of the chain lengths of the terms we encountered along the way.
        for i, x in enumerate(chain):
            known_chain_lengths[x] = chain_length - i
        return chain_length

    def get_answer(self):
        Answer = namedtuple('Answer', ['n', 'chain_length'])
        answer = Answer(None, 0)
        chain_lengths = {13: 10, 40: 9, 20: 8, 10: 7, 5: 6, 16: 5, 8: 4, 4: 3, 2: 2, 1: 1}
        get_chain_length = self.chain_length
        for n in range(1, 1000000):
            if n in chain_lengths:
                continue
            chain_length = get_chain_length(n, chain_lengths)
            if chain_length > answer.chain_length:
                answer = Answer(n, chain_length)
        return answer.n


if __name__ == '__main__':
    Solution14().print_answer()
