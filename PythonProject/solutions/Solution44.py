from solutions.SolutionBase import SolutionBase
from util.sequences import pentagonal_numbers


class Solution44(SolutionBase):
    NUMBER = 44
    VERIFIED_ANSWER = 5482660

    def __init__(self):
        self._pentagonal_numbers = set()
        self._pentagonal_numbers_generator = pentagonal_numbers()
        self._max_pentagonal_number = -1

    def run_tests(self, test_case):
        pass

    def is_pentagonal(self, n):
        while n > self._max_pentagonal_number:
            num = next(self._pentagonal_numbers_generator)
            self._pentagonal_numbers.add(num)
            self._max_pentagonal_number = num
        return n in self._pentagonal_numbers

    def get_answer(self):
        min_diff = 10e100
        pentagonal_numbers_gen = pentagonal_numbers()
        next(pentagonal_numbers_gen)
        candidates = [next(pentagonal_numbers_gen), next(pentagonal_numbers_gen)]
        while len(candidates) > 1:
            i = 0
            highest_candidate = candidates[-1]
            while i < len(candidates) - 1:
                candidate = candidates[i]
                p_diff = highest_candidate - candidate
                if p_diff > min_diff:
                    # since we start at 0 and this list is monotonically increasing, i will always be 0 here.
                    assert i == 0
                    candidates.pop()
                    continue
                p_sum = highest_candidate + candidate
                if p_diff < min_diff and self.is_pentagonal(p_diff) and self.is_pentagonal(p_sum):
                    min_diff = p_diff
                i += 1

            next_candidate = next(pentagonal_numbers_gen)
            if next_candidate - candidates[-1] < min_diff:
                candidates.append(next_candidate)

        assert min_diff is not None
        return min_diff


if __name__ == '__main__':
    Solution44().print_answer()
