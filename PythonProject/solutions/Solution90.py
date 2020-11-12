from itertools import combinations

from solutions.SolutionBase import SolutionBase


class Solution90(SolutionBase):
    NUMBER = 90
    VERIFIED_ANSWER = 1217
    SQUARE_NUMBER_DIGITS = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]

    def run_tests(self, test_case):
        test_case.assertTrue(Solution90.are_cubes_valid((0, 5, 6, 7, 8, 9), (1, 2, 3, 4, 8, 9)))
        test_case.assertTrue(Solution90.are_cubes_valid((0, 5, 6, 7, 8, 9), (1, 2, 3, 4, 6, 7)))
        test_case.assertFalse(Solution90.are_cubes_valid((1, 5, 6, 7, 8, 9), (1, 2, 3, 4, 6, 7)))
        test_case.assertFalse(Solution90.are_cubes_valid((2, 5, 6, 7, 8, 9), (1, 2, 3, 4, 6, 7)))

    @staticmethod
    def are_cubes_valid(cube1, cube2):
        def make_set(cube):
            if 6 in cube or 9 in cube:
                return set(cube + (6, 9))
            return set(cube)

        cube1, cube2 = make_set(cube1), make_set(cube2)
        for first_digit, second_digit in Solution90.SQUARE_NUMBER_DIGITS:
            if not (first_digit in cube1 and second_digit in cube2 or first_digit in cube2 and second_digit in cube1):
                return False
        return True

    def get_answer(self):
        num_valid_cube_arrangements = 0
        for (d1, d2) in combinations(combinations(range(10), 6), 2):
            if Solution90.are_cubes_valid(d1, d2):
                num_valid_cube_arrangements += 1
        return num_valid_cube_arrangements


if __name__ == '__main__':
    Solution90().print_answer()
