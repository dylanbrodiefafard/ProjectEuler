from math import comb

from solutions.SolutionBase import SolutionBase


def hypergeometric_pmf(population, success_states, draws, observed_successes):
    return (comb(success_states, observed_successes) * comb(population - success_states, draws - observed_successes)) \
           / comb(population, draws)


class Solution493(SolutionBase):
    """
    I thought about this problem as a binomial distribution
    The binomial distribution parameters are
    n - the number of independent experiments
    p - the probability of a success
    I defined a success as "selecting a distinct color"
    So the expected value of this distribution will be the expected number of
    distinct colors selected. Exactly what the question is asking.
    In this context,
    n = the number of distinct colors possible (7)
    p = the probability of selecting a distinct color
    The expected value of this distribution will be n*p

    To compute p, I used the hypergeometric distribution for each color.
    Its parameters are
    N - the population size
    K - the number of success states in the population
    n - the number of draws
    k - the number of observed successes
    I defined a success as "selecting the color". Only 1 of this color needs
    to be selected to be considered a selected distinct color in the binomial
    distribution.
    In this context,
    N = 70 (given)
    K = 10 (given)
    n = 20 (given)
    k = at least 1 (implied by definition)
    Since you can't actually set k = at least 1 (it must be a number) I use
    the identity P(X >= 1) = 1 - P(k = 0).
    k = 0
    So now, all that needs to be computed is P(k = 0), which can be found
    online, or computed directly.
    """
    NUMBER = 493
    VERIFIED_ANSWER = '6.818741802'

    def run_tests(self, test_case):
        test_case.assertEqual(0.003964583058015066, hypergeometric_pmf(50, 10, 5, 4))
        test_case.assertEqual(0.00011893749174045196, hypergeometric_pmf(50, 10, 5, 5))

    def get_answer(self):
        binomial_trials = 7
        probability_no_successes = hypergeometric_pmf(70, 10, 20, 0)
        binomial_success_probability = 1 - probability_no_successes  # probability_at_least_1_success
        expected_number_of_distinct_colors = binomial_trials * binomial_success_probability
        return f'{expected_number_of_distinct_colors:.9f}'


if __name__ == '__main__':
    Solution493().print_answer()
