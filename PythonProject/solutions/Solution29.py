from solutions.SolutionBase import SolutionBase


class Solution29(SolutionBase):
    NUMBER = 29
    VERIFIED_ANSWER = 9183

    def run_tests(self, test_case):
        test_case.assertEqual(15, self.num_distinct_terms(5))

    @staticmethod
    def num_distinct_terms(max_power: int):
        powers = {
            a ** b
            for a in range(2, max_power + 1)
            for b in range(2, max_power + 1)
        }
        return len(powers)

    def get_answer(self):
        return self.num_distinct_terms(100)


if __name__ == '__main__':
    Solution29().print_answer()
