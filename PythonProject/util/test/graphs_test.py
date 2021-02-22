from unittest import TestCase

from util.graphs import *


class GraphsTest(TestCase):

    def test_graph(self):
        g = Graph()
        v1, v2 = 'v1', 'v2'
        self.assertSetEqual(set(), set(g.vertices()))
        g.add_edge(v1, v2, weight=3.14)
        self.assertSetEqual({v1, v2}, set(g.vertices()))
        self.assertEqual(3.14, g.weight(v1, v2))
        self.assertEqual(v1, 'v1')
        self.assertEqual(v2, 'v2')
        with self.assertRaises(ValueError):
            g.weight(v2, v1)
        g = Graph()
        g.add_edge(v1, v2, weight=3.14, directed=False)
        self.assertEqual(3.14, g.weight(v1, v2))
        self.assertEqual(3.14, g.weight(v2, v1))

    def test_dijkstra(self):
        g = Graph()
        [v1, v2, v3, v4, v5, v6] = [f'v{i}' for i in range(1, 7)]
        #  v1         v4
        # |  \      /    \
        # |   4    3      2
        # |    \  /        \
        # 4     v3 -- 6 --  v6
        # |    /  \        /
        # |   2    1      3
        # |  /      \    /
        # v2          v5
        g.add_edge(v1, v2, weight=4, directed=False)
        g.add_edge(v1, v3, weight=4, directed=False)
        g.add_edge(v2, v3, weight=2, directed=False)
        g.add_edge(v3, v4, weight=3, directed=False)
        g.add_edge(v3, v5, weight=1, directed=False)
        g.add_edge(v3, v6, weight=6, directed=False)
        g.add_edge(v4, v6, weight=2, directed=False)
        g.add_edge(v5, v6, weight=3, directed=False)
        min_distance, path = dijkstra(g, v1, v6)
        self.assertEqual(8, min_distance)
        self.assertListEqual([v1, v3, v5, v6], path)

    def test_maximal_cliques(self):
        g = Graph()
        [v1, v2, v3, v4, v5, v6] = [f'v{i}' for i in range(1, 7)]
        # v6
        #  \
        #  v4 -- v5
        #   |    |  \
        #   |   |    \
        #  v3 - v2 - v1
        g.add_edge(v1, v2, directed=False)
        g.add_edge(v1, v5, directed=False)
        g.add_edge(v2, v3, directed=False)
        g.add_edge(v2, v5, directed=False)
        g.add_edge(v3, v4, directed=False)
        g.add_edge(v4, v5, directed=False)
        g.add_edge(v4, v6, directed=False)
        expected_maximal_cliques = {
            (v1, v2, v5),
            (v2, v3),
            (v4, v5),
            (v4, v6),
            (v3, v4),
        }
        actual_maximal_cliques = {tuple(sorted(c)) for c in maximal_cliques(g)}
        self.assertCountEqual(expected_maximal_cliques, actual_maximal_cliques)
