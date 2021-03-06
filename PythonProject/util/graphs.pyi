from typing import Optional, List, Set, Dict, Tuple, Hashable, Iterator, TypeVar

HashableT = TypeVar('HashableT', bound=Hashable)

class Graph:
    _neighbours_by_vertex: Dict[HashableT, Set[HashableT]]
    _weights: Dict[Tuple[HashableT, HashableT], float]
    def __init__(self: Graph) -> Graph: ...
    def add_edge(self: Graph, vertex1: HashableT, vertex2: HashableT, directed: bool = False, weight: Optional[float] = None) -> None: ...
    def neighbours(self: Graph, vertex: HashableT) -> Set[HashableT]: ...
    def vertices(self: Graph) -> Set[HashableT]: ...
    def weight(self, vertex1: HashableT, vertex2: HashableT) -> float: ...

def dijkstra(graph: Graph, source: HashableT, destination: Optional[HashableT] = None) -> Tuple[float, List[HashableT]]: ...
def maximal_cliques(graph: Graph, vertices: Optional[Set[HashableT]] = None) -> Iterator[Set[HashableT]]: ...
