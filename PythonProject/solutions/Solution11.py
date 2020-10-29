from solutions.BaseSolution import BaseSolution
from util.functools import prod


class Solution11(BaseSolution):
    NUMBER = 11
    VERIFIED_ANSWER = 70600674

    def run_tests(self, test_case):
        small_grid = [
            [1, 0, 0, 5],
            [1, 2, 1, 1],
            [2, 1, 3, 1],
            [5, 2, 2, 4],
        ]
        test_case.assertEqual(5, self.largest_adjacent_product_in_grid(small_grid, 1))
        test_case.assertEqual(12, self.largest_adjacent_product_in_grid(small_grid, 2))
        test_case.assertEqual(24, self.largest_adjacent_product_in_grid(small_grid, 3))
        test_case.assertEqual(25, self.largest_adjacent_product_in_grid(small_grid, 4))

    @staticmethod
    def largest_adjacent_product_in_grid(grid, num_adjacent_in_product):
        if num_adjacent_in_product == 0 or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        if num_adjacent_in_product == 1:
            return max((max(row) for row in grid))
        assert all(len(grid[0]) == len(row) for row in grid), 'Not all rows are the same length!'

        largest_product = 0
        x_max, y_max = len(grid), len(grid[0])
        n = num_adjacent_in_product - 1
        for x in range(x_max):
            for y in range(y_max):
                if x + n < x_max:
                    largest_product = max(largest_product, prod((grid[x][y] for x in range(x, x + n))))
                if y + n < y_max:
                    largest_product = max(largest_product, prod((grid[x][y] for y in range(y, y + n))))
                if x + n < x_max and y + n < x_max:
                    largest_product = max(largest_product, prod((grid[x + i][y + i] for i in range(num_adjacent_in_product))))
                if x - n >= 0 and y + n < y_max:
                    largest_product = max(largest_product, prod((grid[x - i][y + i] for i in range(num_adjacent_in_product))))
        return largest_product

    def get_answer(self):
        grid = [
            list(map(int, line.strip().split()))
            for line in self.get_lines_from_data_file_in_archive('p011.zip', 'p011_grid.txt')
        ]
        return self.largest_adjacent_product_in_grid(grid, 4)


if __name__ == '__main__':
    Solution11().print_answer()
