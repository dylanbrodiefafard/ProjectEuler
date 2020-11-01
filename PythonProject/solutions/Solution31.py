from solutions.SolutionBase import SolutionBase


class Solution31(SolutionBase):
    NUMBER = 31
    VERIFIED_ANSWER = 73682
    COINS = [1, 2, 5, 10, 20, 50, 100, 200]

    def run_tests(self, test_case):
        test_case.assertEqual(1, self.num_ways_to_make(200, [200]))
        test_case.assertEqual(2, self.num_ways_to_make(200, [100, 200]))
        test_case.assertEqual(0, self.num_ways_to_make(50, [100, 200]))
        test_case.assertEqual(4, self.num_ways_to_make(200, [50, 100, 200]))
        test_case.assertEqual(4, self.num_ways_to_make(200, [50, 100, 200]))
        test_case.assertEqual(11, self.num_ways_to_make(10, self.COINS))

    @staticmethod
    def num_ways_to_make(total_amount: int, coins: list):
        coins = sorted(coins)
        min_coin = coins[0]
        # use this to memoize the number of ways as we build up the solution
        ways_by_amount_and_coin = {}
        for amount in range(min_coin, total_amount + 1):
            for coin_index, coin in enumerate(coins):
                including_coin = excluding_coin = 0
                if amount - coin >= 0:
                    default_ways = 1 if (amount - coin) == 0 else 0
                    including_coin = ways_by_amount_and_coin.setdefault((amount - coin, coin_index), default_ways)
                if coin_index > 0:
                    default_ways = 1 if amount == min_coin else 0
                    excluding_coin = ways_by_amount_and_coin.setdefault((amount, coin_index - 1), default_ways)
                ways_by_amount_and_coin[(amount, coin_index)] = including_coin + excluding_coin
        return ways_by_amount_and_coin.get((total_amount, len(coins) - 1), 0)

    def get_answer(self):
        return self.num_ways_to_make(200, self.COINS)


if __name__ == '__main__':
    Solution31().print_answer()
