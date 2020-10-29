from solutions.BaseSolution import BaseSolution


class Solution14(BaseSolution):
    NUMBER = 14
    VERIFIED_ANSWER = 837799

    def __init__(self):
        self._chain_lengths = {}

    def run_tests(self, test_case):
        test_case.assertEqual(10, self.get_chain_length(13))

    def get_chain_length(self, n):
        chain_length = 1
        x = n
        while x != 1:
            if x % 2 == 0:
                x = x / 2
            else:
                x = x * 3 + 1
            if x in self._chain_lengths:
                chain_length += self._chain_lengths[x]
                break
            chain_length += 1
        self._chain_lengths[n] = chain_length
        return chain_length

    def get_answer(self):
        self._chain_lengths.clear()
        max_chain_length = 0
        max_chain_length_n = None
        for n in range(1, 1000000):
            chain_length = self.get_chain_length(n)
            if chain_length > max_chain_length:
                max_chain_length = chain_length
                max_chain_length_n = n
        return max_chain_length_n


if __name__ == '__main__':
    Solution14().print_answer()
