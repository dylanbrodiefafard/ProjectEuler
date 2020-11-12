from solutions.SolutionBase import SolutionBase
from util.more_itertools import first_true, str_product

DIGITS = '123456789'
ROWS = 'ABCDEFGHI'
COLUMNS = DIGITS
SQUARES = list(str_product(ROWS, COLUMNS))
UNIT_LIST = (
        [list(str_product(ROWS, col)) for col in COLUMNS] +
        [list(str_product(row, COLUMNS)) for row in ROWS] +
        [list(str_product(rows, cols)) for rows in ('ABC', 'DEF', 'GHI') for cols in ('123', '456', '789')]
)
UNITS = {s: [u for u in UNIT_LIST if s in u] for s in SQUARES}
PEERS = {s: set(sum(UNITS[s], [])) - {s} for s in SQUARES}


# Much of the original code for this class is from http://norvig.com/sudoku.html
class SuDokuPuzzle(object):
    def __init__(self, grid):
        self._values = self.parse_grid(grid)
        if self._values is False:
            raise ValueError('Unable to assign given digits to squares.')

    @staticmethod
    def parse_grid(grid):
        """Convert grid to a dict of possible values, {square: digits}, or
        return False if a contradiction is detected."""
        # To start, every square can be any digit; then assign values from the grid.
        chars = [c for c in grid if c in DIGITS or c in '0.']
        assert len(chars) == 81
        values = {s: DIGITS for s in SQUARES}
        for square, digit in zip(SQUARES, chars):
            if digit in DIGITS:
                if not SuDokuPuzzle.assign(values, square, digit):
                    return False  # (Fail if we can't assign d to square s.)
        return values

    @staticmethod
    def assign(values, square, digit):
        """Eliminate all other values (except d) from value[s] and propagate.
        Return values, except return False if a contradiction is detected."""
        other_values = values[square].replace(digit, '')
        if all(SuDokuPuzzle.eliminate(values, square, other_digit) for other_digit in other_values):
            return values
        return False

    @staticmethod
    def eliminate(values, square, digit):
        """Eliminate digits from values[square]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected."""
        if digit not in values[square]:
            return values  # Already eliminated
        values[square] = values[square].replace(digit, '')
        # (1) If a square square is reduced to one value d2, then eliminate d2 from the peers.
        if len(values[square]) == 0:
            return False  # Contradiction: removed last value
        elif len(values[square]) == 1:
            other_digit = values[square]
            if not all(SuDokuPuzzle.eliminate(values, peer_square, other_digit) for peer_square in PEERS[square]):
                return False
        # (2) If a unit is reduced to only one place for a value digits, then put it there.
        for unit in UNITS[square]:
            digit_places = [s for s in unit if digit in values[s]]
            if len(digit_places) == 0:
                return False  # Contradiction: no place for this value
            elif len(digit_places) == 1:
                # digits can only be in one place in unit; assign it there
                if not SuDokuPuzzle.assign(values, digit_places[0], digit):
                    return False
        return values

    @staticmethod
    def search(values):
        """Using depth-first search and propagation, try all possible values."""
        if values is False:
            return False  # Failed earlier
        if all(len(values[s]) == 1 for s in SQUARES):
            return values  # Solved!
        # Chose the unfilled square square with the fewest possibilities
        _, square = min((len(values[s]), s) for s in SQUARES if len(values[s]) > 1)
        return first_true(SuDokuPuzzle.search(SuDokuPuzzle.assign(values.copy(), square, d)) for d in values[square])

    def solve(self):
        values = self.search(self._values)
        if values is False:
            raise ValueError('Unable to solve')
        return ''.join(values[row + col] for row in ROWS for col in COLUMNS)


class Solution96(SolutionBase):
    NUMBER = 96
    VERIFIED_ANSWER = 24702

    def run_tests(self, test_case):
        test_case.assertEqual(81, len(SQUARES))
        test_case.assertEqual(27, len(UNIT_LIST))
        test_case.assertTrue(all(len(UNITS[s]) == 3 for s in SQUARES))
        test_case.assertTrue(all(len(PEERS[s]) == 20 for s in SQUARES))
        test_case.assertListEqual([
            ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
            ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        ], UNITS['C2'])
        test_case.assertSetEqual({
            'A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'A1', 'A3', 'B1', 'B3'
        }, PEERS['C2'])
        puzzle = SuDokuPuzzle('003020600900305001001806400008102900700000008006708200002609500800203009005010300')
        test_case.assertEqual('483921657967345821251876493548132976729564138136798245372689514814253769695417382', puzzle.solve())

    def get_answer(self):
        answer = 0
        grid = ''
        for i, line in enumerate(self.get_lines_from_data_file_in_archive('p096.zip', 'p096_sudoku.txt')):
            if i % 10 == 0:
                continue
            grid += line
            if len(grid) == 81:
                answer += int(SuDokuPuzzle(grid).solve()[:3])
                grid = ''
        return answer


if __name__ == '__main__':
    Solution96().print_answer()
