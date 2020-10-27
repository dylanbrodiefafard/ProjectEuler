from solutions.BaseSolution import BaseSolution


class P57(BaseSolution):
    NUMBER = 57
    VERIFIED_ANSWER = 153

    def run_tests(self, test_case):
        test_case.assertEqual(0, self.num_numerator_has_more_digits(0))
        test_case.assertEqual(0, self.num_numerator_has_more_digits(1))
        test_case.assertEqual(0, self.num_numerator_has_more_digits(2))
        test_case.assertEqual(0, self.num_numerator_has_more_digits(3))
        test_case.assertEqual(0, self.num_numerator_has_more_digits(4))
        test_case.assertEqual(0, self.num_numerator_has_more_digits(5))
        test_case.assertEqual(0, self.num_numerator_has_more_digits(6))
        test_case.assertEqual(0, self.num_numerator_has_more_digits(7))
        test_case.assertEqual(1, self.num_numerator_has_more_digits(8))

    @staticmethod
    def num_numerator_has_more_digits(num_expansions):
        num_numerators_with_more_digits = 0

        p = q = 1  # first expansion
        num_expansions -= 1
        while True:
            if num_expansions < 0:
                return num_numerators_with_more_digits
            p_next, q_next = p + 2 * q,  p + q
            p, q = p_next, q_next
            if len(str(p)) > len(str(q)):
                num_numerators_with_more_digits += 1
            num_expansions -= 1

    def get_answer(self):
        return self.num_numerator_has_more_digits(1000)


if __name__ == '__main__':
    P57().print_answer()
