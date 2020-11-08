from __future__ import annotations
from typing import List, Optional
from heapdict import heapdict


class Vertex(object):
    __slots__ = ['_name', '_neighbors']

    def __init__(self, name: str):
        self._name = name
        self._neighbors = set()

    def __str__(self):
        return self.name

    __repr__ = __str__

    def __iter__(self):
        return iter(self._neighbors)

    @property
    def name(self):
        return self._name

    def add_neighbour(self, neighbour: Vertex):
        self._neighbors.add(neighbour)


class Graph(object):
    __slots__ = ['_vertices_by_name', '_distances']

    def __init__(self):
        self._vertices_by_name = {}
        self._distances = {}

    def __iter__(self):
        return iter(self._vertices_by_name.values())

    def add_edge(self, vertex1: Vertex, vertex2: Vertex, distance: float, directed: bool = True) -> None:
        if vertex1.name in self._vertices_by_name and vertex1 != self._vertices_by_name[vertex1.name]:
            raise ValueError(f'Vertex "{vertex1.name}" already exists!')
        if vertex2.name in self._vertices_by_name and vertex2 != self._vertices_by_name[vertex2.name]:
            raise ValueError(f'Vertex "{vertex2.name}" already exists!')

        vertex1.add_neighbour(vertex2)
        self._vertices_by_name[vertex1.name] = vertex1
        self._vertices_by_name[vertex2.name] = vertex2
        self._distances[(vertex1, vertex2)] = distance
        if not directed:
            vertex2.add_neighbour(vertex1)
            self._distances[(vertex2, vertex1)] = distance

    def vertex(self, name: str, create: bool = False) -> Vertex:
        if name not in self._vertices_by_name:
            if create:
                self._vertices_by_name[name] = Vertex(name)
            else:
                raise ValueError(f'Vertex "{name}" does not exist.')
        return self._vertices_by_name[name]

    def distance(self, vertex1: Vertex, vertex2: Vertex) -> float:
        if (vertex1, vertex2) not in self._distances:
            raise ValueError(f'No edge between {vertex1} and {vertex2}.')
        return self._distances[(vertex1, vertex2)]


def dijkstra(graph: Graph, source: Vertex, destination: Optional[Vertex] = None) -> (float, List[Vertex]):
    dist = {}
    prev = {}
    queue = heapdict()

    for vertex in graph:
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
        for v in u:
            if v not in queue:
                continue
            if (alt := dist[u] + graph.distance(u, v)) < dist[v]:
                queue[v] = dist[v] = alt
                prev[v] = u

    if destination:
        raise ValueError(f'{destination} is unreachable from {source}.')

    return dist, prev
