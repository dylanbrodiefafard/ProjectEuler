from typing import List, Optional

from solutions.SolutionBase import SolutionBase


class Solution81(SolutionBase):
    SMALL_MATRIX: List[List[int]]
    @staticmethod
    def minimal_path_sum(matrix: List[List[int]]) -> Optional[int]: ...
    @staticmethod
    def matrix_from_lines(lines: List[str]) -> List[List[int]]: ...