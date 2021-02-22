from solutions.SolutionBase import SolutionBase
from util.graphs import Graph, maximal_cliques
from util.primes import is_prime
from util.sequences import prime_numbers


class Solution60(SolutionBase):
    NUMBER = 60
    VERIFIED_ANSWER = 26033

    def run_tests(self, test_case):
        test_case.assertEqual(10, self.minimum_sum_of_prime_pair_sets(2))
        test_case.assertEqual(107, self.minimum_sum_of_prime_pair_sets(3))
        test_case.assertEqual(792, self.minimum_sum_of_prime_pair_sets(4))

    @staticmethod
    def minimum_sum_of_prime_pair_sets(n):
        assert n > 1
        known_primes = set()
        g = Graph()
        for prime_number in prime_numbers():
            if prime_number in (2, 5):
                continue
            for other_prime in known_primes:
                if not Solution60.is_prime_pair(other_prime, prime_number):
                    continue
                g.add_edge(prime_number, other_prime, directed=False)

                for maximal_clique in maximal_cliques(g, g.neighbours(prime_number) | g.neighbours(other_prime)):
                    if len(maximal_clique) < n:
                        continue
                    clique_sum = sum(sorted(v for v in maximal_clique)[:n])
                    return clique_sum

            known_primes.add(prime_number)

    @staticmethod
    def is_prime_pair(prime_number1, prime_number2):
        assert prime_number1 < prime_number2
        if prime_number1 > 3 and prime_number2 - prime_number1 == 2:
            # concatenating twin primes always results in a number divisible by 3
            return False
        digits1 = str(prime_number1)
        digits2 = str(prime_number2)
        return is_prime(int(digits1 + digits2)) and is_prime(int(digits2 + digits1))

    def get_answer(self):
        return self.minimum_sum_of_prime_pair_sets(5)


if __name__ == '__main__':
    Solution60().print_answer()
