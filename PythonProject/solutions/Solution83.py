from typing import List

from solutions.Solution81 import Solution81
from solutions.Solution82 import Solution82
from solutions.SolutionBase import SolutionBase
from util.graphs import dijkstra, Graph


class Solution83(SolutionBase):
    NUMBER = 83
    VERIFIED_ANSWER = 425185
    DIRECTION_KWARGS = {'up': True, 'down': True, 'left': True, 'right': True}

    def run_tests(self, test_case):
        g = Solution82.graph_from_matrix(Solution81.SMALL_MATRIX, **self.DIRECTION_KWARGS)
        self.add_start_and_end_edges(g, Solution81.SMALL_MATRIX)
        expected_path = [g.vertex('start'), g.vertex('(0, 0)'), g.vertex('(1, 0)'), g.vertex('(1, 1)'),
                         g.vertex('(1, 2)'), g.vertex('(0, 2)'), g.vertex('(0, 3)'), g.vertex('(0, 4)'),
                         g.vertex('(1, 4)'), g.vertex('(2, 4)'), g.vertex('(2, 3)'), g.vertex('(3, 3)'),
                         g.vertex('(4, 3)'), g.vertex('(4, 4)'), g.vertex('end')]
        distance, path = dijkstra(g, g.vertex('start'), g.vertex('end'))
        test_case.assertEqual(2297, distance)
        test_case.assertListEqual(expected_path, path)

    @staticmethod
    def add_start_and_end_edges(graph: Graph, matrix: List[List[int]]) -> None:
        graph.add_edge(graph.vertex('start', create=True), graph.vertex(str((0, 0))), matrix[0][0])
        graph.add_edge(graph.vertex(str((len(matrix) - 1, len(matrix[-1]) - 1))), graph.vertex('end', create=True), 0)

    def get_answer(self):
        matrix = Solution81.matrix_from_lines(self.get_lines_from_data_file_in_archive('p083.zip', 'p083_matrix.txt'))
        g = Solution82.graph_from_matrix(matrix, **self.DIRECTION_KWARGS)
        self.add_start_and_end_edges(g, matrix)
        distance, _ = dijkstra(g, g.vertex('start'), g.vertex('end'))
        return distance


if __name__ == '__main__':
    Solution83().print_answer()
