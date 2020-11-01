from collections import Counter

from solutions.SolutionBase import SolutionBase


class HandRank:
    ROYAL_FLUSH = 'Royal flush'
    STRAIGHT_FLUSH = 'Straight flush'
    FOUR_OF_A_KIND = 'Four of a kind'
    FULL_HOUSE = 'Full house'
    FLUSH = 'Flush'
    STRAIGHT = 'Straight'
    THREE_OF_A_KIND = 'Three of a kind'
    TWO_PAIR = 'Two pair'
    PAIR = 'Pair'
    HIGH_CARD = 'High card'

    RANK_ORDER = [
        HIGH_CARD,
        PAIR,
        TWO_PAIR,
        THREE_OF_A_KIND,
        STRAIGHT,
        FLUSH,
        FULL_HOUSE,
        FOUR_OF_A_KIND,
        STRAIGHT_FLUSH,
        ROYAL_FLUSH,
    ]

    # noinspection SpellCheckingInspection
    VALUE_MAP = {v: (i + 1) for i, v in enumerate('123456789TJQKA')}


class FiveCardPokerHand(object):
    def __init__(self, cards):
        values = []
        all_same_suit = True
        for i, (value, suit) in enumerate(cards):
            values.append(HandRank.VALUE_MAP[value])
            if i > 0 and all_same_suit:
                all_same_suit &= cards[i - 1][-1] == suit  # Is this suit same as all previous suits?
        values.sort(reverse=True)

        all_consecutive = (
            (5 if values[4] == 14 else values[4]) - values[3] == 1 and
            values[3] - values[2] == 1 and values[2] - values[1] == 1 and values[1] - values[0] == 1
        )

        value_counts = Counter(values)
        two_most_common_counts = [count for _, count in value_counts.most_common(2)]
        most_common_count = two_most_common_counts[0]

        if all_same_suit and all_consecutive and values[0] == 10:
            self.rank = HandRank.ROYAL_FLUSH
        elif all_same_suit and all_consecutive:
            self.rank = HandRank.STRAIGHT_FLUSH
        elif most_common_count == 4:
            self.rank = HandRank.FOUR_OF_A_KIND
        elif two_most_common_counts == [3, 2]:
            self.rank = HandRank.FULL_HOUSE
        elif all_same_suit:
            self.rank = HandRank.FLUSH
        elif all_consecutive:
            self.rank = HandRank.STRAIGHT
        elif most_common_count == 3:
            self.rank = HandRank.THREE_OF_A_KIND
        elif two_most_common_counts == [2, 2]:
            self.rank = HandRank.TWO_PAIR
        elif most_common_count == 2:
            self.rank = HandRank.PAIR
        else:
            self.rank = HandRank.HIGH_CARD
        self.rank_order = HandRank.RANK_ORDER.index(self.rank)
        self.rank_sorted_values = [val for val, _ in value_counts.most_common()]

    def less_than(self, other):
        if self.rank == other.rank:
            return self.rank_sorted_values < other.rank_sorted_values
        return self.rank_order < other.rank_order


class P54(SolutionBase):
    NUMBER = 54
    VERIFIED_ANSWER = 379

    def run_tests(self, test_case):
        test_case.assertEqual(2, self.get_winner('5H 5C 6S 7S KD 2C 3S 8S 8D TD'))
        test_case.assertEqual(1, self.get_winner('5D 8C 9S JS AC 2C 5C 7D 8S QH'))
        test_case.assertEqual(2, self.get_winner('2D 9C AS AH AC 3D 6D 7D TD QD'))
        test_case.assertEqual(1, self.get_winner('4D 6S 9H QH QC 3D 6D 7H QD QS'))
        test_case.assertEqual(1, self.get_winner('2H 2D 4C 4D 4S 3C 3D 3S 9S 9D'))

    @staticmethod
    def get_winner(line):
        cards = line.strip().split(' ')
        return 2 if FiveCardPokerHand(cards[:5]).less_than(FiveCardPokerHand(cards[5:])) else 1

    def get_answer(self):
        player1_wins = 0
        for line in self.get_lines_from_data_file_in_archive('p054.zip', 'p054_poker.txt'):
            if self.get_winner(line) == 1:
                player1_wins += 1
        return player1_wins


if __name__ == '__main__':
    P54().print_answer()
