from typing import List

from solutions.Solution81 import Solution81
from solutions.SolutionBase import SolutionBase
from util.graphs import Graph, dijkstra


class Solution82(SolutionBase):
    NUMBER = 82
    VERIFIED_ANSWER = 260324
    DIRECTION_KWARGS = {'up': True, 'down': True, 'right': True}

    def run_tests(self, test_case):
        g = self.graph_from_matrix(Solution81.SMALL_MATRIX, **self.DIRECTION_KWARGS)
        self.add_start_and_end_edges(g, Solution81.SMALL_MATRIX)
        expected_path = [g.vertex('start'), g.vertex('(1, 0)'), g.vertex('(1, 1)'), g.vertex('(1, 2)'),
                         g.vertex('(0, 2)'), g.vertex('(0, 3)'), g.vertex('(0, 4)'), g.vertex('end')]
        distance, path = dijkstra(g, g.vertex('start'), g.vertex('end'))
        test_case.assertEqual(994, distance)
        test_case.assertListEqual(expected_path, path)

    @staticmethod
    def graph_from_matrix(matrix: List[List[int]], up=False, down=False, left=False, right=False) -> Graph:
        g = Graph()
        num_rows = len(matrix)
        for row_i, row in enumerate(matrix):
            num_cols = len(row)
            for col_i, val in enumerate(row):
                v = g.vertex(str((row_i, col_i)), create=True)
                if up and row_i > 0:
                    val_up = matrix[row_i - 1][col_i]
                    g.add_edge(v, g.vertex(str((row_i - 1, col_i)), create=True), val_up)
                if down and row_i < num_rows - 1:
                    val_down = matrix[row_i + 1][col_i]
                    g.add_edge(v, g.vertex(str((row_i + 1, col_i)), create=True), val_down)
                if left and col_i > 0:
                    val_left = row[col_i - 1]
                    g.add_edge(v, g.vertex(str((row_i, col_i - 1)), create=True), val_left)
                if right and col_i < num_cols - 1:
                    val_right = row[col_i + 1]
                    g.add_edge(v, g.vertex(str((row_i, col_i + 1)), create=True), val_right)
        return g

    @staticmethod
    def add_start_and_end_edges(graph: Graph, matrix: List[List[int]]) -> None:
        for row_i in range(len(matrix)):
            graph.add_edge(graph.vertex('start', create=True), graph.vertex(str((row_i, 0))), matrix[row_i][0])
            graph.add_edge(graph.vertex(str((row_i, len(matrix[row_i]) - 1))), graph.vertex('end', create=True), 0)

    def get_answer(self):
        matrix = Solution81.matrix_from_lines(self.get_lines_from_data_file_in_archive('p082.zip', 'p082_matrix.txt'))
        g = self.graph_from_matrix(matrix, **self.DIRECTION_KWARGS)
        self.add_start_and_end_edges(g, matrix)
        distance, _ = dijkstra(g, g.vertex('start'), g.vertex('end'))
        return distance


if __name__ == '__main__':
    Solution82().print_answer()
