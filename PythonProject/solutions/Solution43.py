from solutions.BaseSolution import BaseSolution


class Solution43(BaseSolution):
    NUMBER = 43
    VERIFIED_ANSWER = 16695334890
    DIVISORS = [2, 3, 5, 7, 11, 13, 17]
    ALL_DIGITS = set(range(10))

    def run_tests(self, test_case):
        test_case.assertIn(
            (7, 2, 8, 9),
            set(self.numbers_with_property({9}, (7, 2, 8), 9))
        )
        test_case.assertIn(
            (5, 7, 2, 8, 9),
            set(self.numbers_with_property({8, 9}, (5, 7, 2), 8))
        )
        test_case.assertIn(
            (3, 5, 7, 2, 8, 9),
            set(self.numbers_with_property({8, 9, 2}, (3, 5, 7), 7))
        )

    def numbers_with_property(self, available_digits, prev_comb, index):
        for n in available_digits:
            # number can't start with a 0
            if index == 0 and n == 0:
                continue
            comb = prev_comb + (n, )
            if index > 2:
                digits = int(''.join(map(str, comb[-3:])))
                if digits % self.DIVISORS[index - 3] != 0:
                    continue
            if index == 9:
                yield comb
                continue
            yield from self.numbers_with_property(available_digits - {n}, comb, index + 1)

    def get_answer(self):
        total = 0
        for number in self.numbers_with_property(set(range(10)), (), 0):
            total += int(''.join(map(str, number)))
        return total


if __name__ == '__main__':
    Solution43().print_answer()
