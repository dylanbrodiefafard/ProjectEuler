from collections import defaultdict
from itertools import takewhile

from solutions.SolutionBase import SolutionBase
from util.sequences import triangular_numbers, octagonal_numbers, heptagonal_numbers, hexagonal_numbers, pentagonal_numbers, squares


class Solution61(SolutionBase):
    NUMBER = 61
    VERIFIED_ANSWER = 28684
    GENERATORS = (triangular_numbers, squares, pentagonal_numbers, hexagonal_numbers, heptagonal_numbers, octagonal_numbers)

    def run_tests(self, test_case):
        test_case.assertSetEqual({8128, 2882, 8281}, self.cyclical_figurate_numbers(3))

    @staticmethod
    def cyclical_figurate_numbers(num_numbers: int):
        assert 1 < num_numbers < 7
        digit_min_limit, digit_max_limit = 10 ** (4 - 1) - 1, 10 ** 4
        # Generate the numbers for the polygonal types
        triangle_numbers = set()
        polygonal_number_types = []
        for i in range(num_numbers):
            gen = Solution61.GENERATORS[i]
            polygonal_numbers = {str(n) for n in takewhile(lambda n: n < digit_max_limit, gen()) if n > digit_min_limit}
            if i == 0:
                triangle_numbers.update(polygonal_numbers)
            else:
                polygonal_number_types.append(polygonal_numbers)

        # Create maps from first digits to sets of last digits for each polygonal type
        # (excluding triangle because we are going to start with those.)
        first_to_last_digits_all_polygonal_type = [defaultdict(set) for _ in range(len(polygonal_number_types))]
        for i, first_to_last_digits in enumerate(first_to_last_digits_all_polygonal_type):
            for n in polygonal_number_types[i]:
                first_digits, last_digits = n[:2], n[-2:]
                first_to_last_digits[first_digits].add(last_digits)

        # Since these numbers are cyclical, we can start with any polygonal type we want. Let's start with triangle numbers
        for t in triangle_numbers:
            first_triangle_digits, last_triangle_digits = t[:2], t[-2:]
            # This stack will represent the
            # (
            #   last digits of the previous number,
            #   all polygonal type maps of first digits to last digits,
            #   the current set of numbers found,
            #  )
            stack = [(last_triangle_digits, first_to_last_digits_all_polygonal_type, (t, ))]
            while stack:
                last_digits, first_to_last_digits_other_polygonal_types, cyclical_numbers = stack.pop()
                for first_to_last_digits in first_to_last_digits_other_polygonal_types:
                    # We found a match of last digits of the current number to the first digits on another number in a different polygonal group
                    for next_last_digits in first_to_last_digits[last_digits]:
                        prev_last_digits = cyclical_numbers[-1][-2:]
                        next_cyclical_numbers = cyclical_numbers + (prev_last_digits + next_last_digits,)
                        if len(next_cyclical_numbers) == num_numbers and first_triangle_digits == next_last_digits:
                            # We found our answer!
                            return set(map(int, next_cyclical_numbers))
                        # Add to the stack to keep searching. Remember to remove this map because we've now used it.
                        next_number_sets = list(first_to_last_digits_other_polygonal_types)
                        next_number_sets.remove(first_to_last_digits)
                        stack.append((next_last_digits, next_number_sets, next_cyclical_numbers))

    def get_answer(self):
        return sum(self.cyclical_figurate_numbers(6))


if __name__ == '__main__':
    Solution61().print_answer()
