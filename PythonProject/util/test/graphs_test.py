from unittest import TestCase

from util.graphs import *


class GraphsTest(TestCase):
    def test_vertex(self):
        v1, v2 = Vertex('v1'), Vertex('v2')
        self.assertSetEqual(set(), set(v1))
        v1.add_neighbour(v2)
        self.assertSetEqual({v2}, set(v1))
        self.assertSetEqual(set(), set(v2))
        v2.add_neighbour(v1)
        self.assertSetEqual({v2}, set(v1))
        self.assertSetEqual({v1}, set(v2))

    def test_graph(self):
        g = Graph()
        v1, v2 = Vertex('v1'), Vertex('v2')
        self.assertSetEqual(set(), set(g))
        g.add_edge(v1, v2, 3.14)
        self.assertSetEqual({v1, v2}, set(g))
        self.assertEqual(3.14, g.distance(v1, v2))
        self.assertEqual(v1, g.vertex('v1'))
        self.assertEqual(v2, g.vertex('v2'))
        with self.assertRaises(ValueError):
            g.distance(v2, v1)
        g = Graph()
        g.add_edge(v1, v2, 3.14, directed=False)
        self.assertEqual(3.14, g.distance(v1, v2))
        self.assertEqual(3.14, g.distance(v2, v1))

    def test_dijkstra(self):
        g = Graph()
        [v1, v2, v3, v4, v5, v6] = [Vertex(f'v{i}') for i in range(1, 7)]
        #  v1         v4
        # |  \      /    \
        # |   4    3      2
        # |    \  /        \
        # 4     v3 -- 6 --  v6
        # |    /  \        /
        # |   2    1      3
        # |  /      \    /
        # v2          v5
        g.add_edge(v1, v2, 4, directed=False)
        g.add_edge(v1, v3, 4, directed=False)
        g.add_edge(v2, v3, 2, directed=False)
        g.add_edge(v3, v4, 3, directed=False)
        g.add_edge(v3, v5, 1, directed=False)
        g.add_edge(v3, v6, 6, directed=False)
        g.add_edge(v4, v6, 2, directed=False)
        g.add_edge(v5, v6, 3, directed=False)
        min_distance, path = dijkstra(g, v1, v6)
        self.assertEqual(8, min_distance)
        self.assertListEqual([v1, v3, v5, v6], path)
