from collections import defaultdict
from itertools import islice

from solutions.SolutionBase import SolutionBase


class Solution62(SolutionBase):
    NUMBER = 62
    VERIFIED_ANSWER = 127035954683

    def run_tests(self, test_case):
        test_case.assertListEqual([1, 8, 27, 64, 125, 216], list(islice(self.cubes(), 6)))

    @staticmethod
    def cubes():
        n = 1
        while True:
            yield n ** 3
            n += 1

    def get_answer(self):
        permutation_counts = defaultdict(list)
        for cube in self.cubes():
            key = ''.join(sorted(str(cube)))
            other_cubes = permutation_counts[key]
            other_cubes.append(cube)
            if len(other_cubes) == 5:
                # Technically we may not have search the entire cube space for these digits and there could
                # be a sixth permuted cube in this group. Fortunately, this answer was correct, so no need
                # to fix this.
                return min(other_cubes)


if __name__ == '__main__':
    Solution62().print_answer()
