from itertools import islice, permutations

from solutions.BaseSolution import BaseSolution


class Solution24(BaseSolution):
    NUMBER = 24
    VERIFIED_ANSWER = 2783915460

    def run_tests(self, test_case):
        test_case.assertEqual('012', self.nth_lexicographic_permutation({0, 1, 2}, 1))
        test_case.assertEqual('021', self.nth_lexicographic_permutation({0, 1, 2}, 2))
        test_case.assertEqual('102', self.nth_lexicographic_permutation({0, 1, 2}, 3))
        test_case.assertEqual('120', self.nth_lexicographic_permutation({0, 1, 2}, 4))
        test_case.assertEqual('201', self.nth_lexicographic_permutation({0, 1, 2}, 5))
        test_case.assertEqual('210', self.nth_lexicographic_permutation({0, 1, 2}, 6))

    @staticmethod
    def nth_lexicographic_permutation(digits, n):
        permutation_string = ''.join(map(str, sorted(digits)))
        nth_digits = next(islice(permutations(permutation_string, len(digits)), n - 1, None))
        return ''.join(nth_digits)

    def get_answer(self):
        return int(self.nth_lexicographic_permutation(range(0, 10), 1000000))


if __name__ == '__main__':
    Solution24().print_answer()
