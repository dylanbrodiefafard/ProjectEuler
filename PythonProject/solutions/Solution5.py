from solutions.BaseSolution import BaseSolution


class Solution5(BaseSolution):
    NUMBER = 5
    VERIFIED_ANSWER = 232792560

    def run_tests(self, test_case):
        test_case.assertEqual(2520, self.smallest_number_evenly_divisible_by_all(1, 10))

    @staticmethod
    def divisible_by_all_numbers(n, min_val, max_val):
        for m in range(max_val, min_val - 1, -1):
            if not n % m == 0:
                return False
        return True

    @staticmethod
    def smallest_number_evenly_divisible_by_all(min_val, max_val):
        n = max_val
        while True:
            if Solution5.divisible_by_all_numbers(n, min_val, max_val):
                return n
            n += max_val

    def get_answer(self):
        return self.smallest_number_evenly_divisible_by_all(1, 20)


if __name__ == '__main__':
    Solution5().print_answer()
