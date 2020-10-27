from solutions.BaseSolution import BaseSolution
from util.integers import is_paldindrome


class P55(BaseSolution):
    NUMBER = 55
    VERIFIED_ANSWER = 249

    def run_tests(self, test_case):
        pass

    @staticmethod
    def is_lychrel(n):
        n = n + int(str(n)[::-1])
        steps = 1
        while steps <= 50:
            if is_paldindrome(n):
                return False
            n = n + int(str(n)[::-1])
            steps += 1
        return True

    def get_answer(self):
        num_lychrel = 0
        for n in range(0, 10001):
            if self.is_lychrel(n):
                num_lychrel += 1
        return num_lychrel


if __name__ == '__main__':
    P55().print_answer()
