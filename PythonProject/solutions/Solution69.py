from solutions.SolutionBase import SolutionBase
from util.sequences import prime_numbers


class Solution69(SolutionBase):
    NUMBER = 69
    VERIFIED_ANSWER = 510510

    def run_tests(self, test_case):
        test_case.assertEqual(6, self.get_maximum(10))

    @staticmethod
    def get_maximum(max_n):
        # For each primorial n, the fraction n/φ(n) is larger than any smaller n, where φ is the Euler totient function.
        # Therefore, the answer will be the largest primorial <= max_n
        assert max_n >= 2
        n = 1
        for p in prime_numbers():
            if (next_n := n * p) > max_n:
                return n
            n = next_n

    def get_answer(self):
        return self.get_maximum(1_000_000)


if __name__ == '__main__':
    Solution69().print_answer()
