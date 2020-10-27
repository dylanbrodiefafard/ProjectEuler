import unittest

from solutions.BaseSolution import BaseSolution


def make_solution_f(s: type):
    def f(test_case: unittest.TestCase):
        solution = s()
        solution.run_tests(test_case)

    return f


def make_verified_answer_f(s: type):
    def f(test_case: unittest.TestCase):
        solution = s()
        test_case.assertIsNotNone(solution.VERIFIED_ANSWER)
        test_case.assertEqual(solution.VERIFIED_ANSWER, solution.get_answer())

    return f


SOLUTION_TESTS = {}
VERIFIED_ANSWER_TESTS = {}

for s_class in BaseSolution.get_solution_classes():
    solution_f_name = 'test_solution{}'.format(s_class.NUMBER)
    SOLUTION_TESTS[solution_f_name] = make_solution_f(s_class)
    SOLUTION_TESTS[solution_f_name].__name__ = solution_f_name

    verified_answer_f_name = 'test_solution{}_answer'.format(s_class.NUMBER)
    VERIFIED_ANSWER_TESTS[verified_answer_f_name] = make_verified_answer_f(s_class)
    VERIFIED_ANSWER_TESTS[verified_answer_f_name].__name__ = verified_answer_f_name


class SolutionsMeta(type):
    TESTS = {}

    def __init__(cls, *args, **kwargs):
        for attr, value in cls.TESTS.items():
            setattr(cls, attr, value)
        super().__init__(*args, **kwargs)


class SolutionsVerifiedAnswersTest(unittest.TestCase, metaclass=SolutionsMeta):
    TESTS = VERIFIED_ANSWER_TESTS


class SolutionsTest(unittest.TestCase, metaclass=SolutionsMeta):
    TESTS = SOLUTION_TESTS


if __name__ == '__main__':
    unittest.main()
