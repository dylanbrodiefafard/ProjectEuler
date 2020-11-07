from solutions.SolutionBase import SolutionBase
from util.primes import primes_up_to


class Solution50(SolutionBase):
    NUMBER = 50
    VERIFIED_ANSWER = 997651

    def run_tests(self, test_case):
        test_case.assertEqual((0, 0), self.longest_prime_sum_of_consecutive_primes(1))
        test_case.assertEqual((2, 1), self.longest_prime_sum_of_consecutive_primes(3))
        test_case.assertEqual((2, 1), self.longest_prime_sum_of_consecutive_primes(4))
        test_case.assertEqual((41, 6), self.longest_prime_sum_of_consecutive_primes(100))
        test_case.assertEqual((953, 21), self.longest_prime_sum_of_consecutive_primes(1000))

    @staticmethod
    def longest_prime_sum_of_consecutive_primes(below: int):
        best_prime_sum, best_length = 0, 0
        primes = list(primes_up_to(below - 1))
        primes_set = set(primes)
        num_primes = len(primes)

        for i in range(0, num_primes):
            prime_sum = 0
            if num_primes - i < best_length:
                # There are not enough primes left to find a better answer.
                break
            for j in range(i, num_primes):
                prime_sum += primes[j]
                if prime_sum >= below:
                    # The sum is too large and will only continue to increase. Stop the loop.
                    break
                if (length := j - i + 1) <= best_length:
                    # The current length is too short to beat the best, so continue.
                    continue
                if prime_sum in primes_set:
                    best_prime_sum, best_length = prime_sum, length

        return best_prime_sum, best_length

    def get_answer(self):
        return self.longest_prime_sum_of_consecutive_primes(1000000)[0]


if __name__ == '__main__':
    Solution50().print_answer()
