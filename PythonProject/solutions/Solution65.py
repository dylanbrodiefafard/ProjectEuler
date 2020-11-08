from solutions.SolutionBase import SolutionBase
from util.integers import simplified_continued_fraction


class Solution65(SolutionBase):
    NUMBER = 65
    VERIFIED_ANSWER = 272

    def run_tests(self, test_case):
        test_case.assertTupleEqual((2, 1), self.nth_continued_fraction_of_e(1))
        test_case.assertTupleEqual((3, 1), self.nth_continued_fraction_of_e(2))
        test_case.assertTupleEqual((8, 3), self.nth_continued_fraction_of_e(3))
        test_case.assertTupleEqual((11, 4), self.nth_continued_fraction_of_e(4))
        test_case.assertTupleEqual((19, 7), self.nth_continued_fraction_of_e(5))
        test_case.assertTupleEqual((87, 32), self.nth_continued_fraction_of_e(6))
        test_case.assertTupleEqual((106, 39), self.nth_continued_fraction_of_e(7))
        test_case.assertTupleEqual((193, 71), self.nth_continued_fraction_of_e(8))
        test_case.assertTupleEqual((1264, 465), self.nth_continued_fraction_of_e(9))
        test_case.assertTupleEqual((1457, 536), self.nth_continued_fraction_of_e(10))

    @staticmethod
    def terms_of_simple_continued_fraction_of_e():
        yield 1
        n = 2
        while True:
            yield n
            yield 1
            yield 1
            n += 2

    @staticmethod
    def nth_continued_fraction_of_e(n: int):
        return simplified_continued_fraction(Solution65.terms_of_simple_continued_fraction_of_e(), 2, n - 1)

    def get_answer(self):
        return sum(map(int, str(self.nth_continued_fraction_of_e(100)[0])))


if __name__ == '__main__':
    Solution65().print_answer()
