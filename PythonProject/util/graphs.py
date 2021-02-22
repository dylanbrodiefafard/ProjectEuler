from collections import defaultdict

from heapdict import heapdict


class Graph(object):
    __slots__ = ['_neighbours_by_vertex', '_weights']

    def __init__(self):
        self._neighbours_by_vertex = defaultdict(set)
        self._weights = {}

    def add_edge(self, vertex1, vertex2, directed=True, weight=None):
        self._neighbours_by_vertex[vertex1].add(vertex2)
        other_neighbours = self._neighbours_by_vertex[vertex2]
        if not directed:
            other_neighbours.add(vertex1)
        if weight is not None:
            self._weights[(vertex1, vertex2)] = weight
            if not directed:
                self._weights[(vertex2, vertex1)] = weight

    def neighbours(self, vertex):
        return self._neighbours_by_vertex[vertex]

    def vertices(self):
        return set(self._neighbours_by_vertex.keys())

    def weight(self, vertex1, vertex2):
        if (vertex1, vertex2) not in self._weights:
            raise ValueError(f'No edge between {vertex1} and {vertex2}.')
        return self._weights[(vertex1, vertex2)]


def dijkstra(graph, source, destination=None):
    dist = {}
    prev = {}
    queue = heapdict()

    for vertex in graph.vertices():
        dist[vertex] = float('+inf')
        prev[vertex] = None
        queue[vertex] = dist[vertex]
    queue[source] = dist[source] = 0

    while queue:
        u, _ = queue.popitem()
        if destination and u is destination:
            path = []
            u = destination
            if prev[u] is not None or u == source:
                while u is not None:
                    path.insert(0, u)
                    u = prev[u]
            return dist[destination], path
        for v in graph.neighbours(u):
            if v not in queue:
                continue
            if (alt := dist[u] + graph.weight(u, v)) < dist[v]:
                queue[v] = dist[v] = alt
                prev[v] = u

    if destination:
        raise ValueError(f'{destination} is unreachable from {source}.')

    return dist, prev


def maximal_cliques(graph, vertices=None):
    """A clique, C, in an undirected graph G = (V, E) is a subset of the vertices,
    C ⊆ V, such that every two distinct vertices are adjacent.

    This is equivalent to the condition that the induced subgraph of G induced by C is a complete graph.
    In some cases, the term clique may also refer to the subgraph directly.

    A maximal clique is a clique that cannot be extended by including one more adjacent vertex, that is,
    a clique which does not exist exclusively within the vertex set of a larger clique.

    Reference: https://arxiv.org/pdf/1006.5440.pdf
    """
    if vertices is None:
        vertices = set(graph.vertices())

    stack = [(vertices, set(), set())]
    while stack:
        candidates, clique, excluded = stack.pop()

        if not candidates:
            if not excluded:
                yield clique
            continue

        pivot = max(candidates | excluded, key=lambda _v: len(candidates & graph.neighbours(_v)))
        for v in candidates - graph.neighbours(pivot):
            v_neighbours = graph.neighbours(v)
            stack.append((candidates & v_neighbours, clique | {v}, excluded & v_neighbours))
