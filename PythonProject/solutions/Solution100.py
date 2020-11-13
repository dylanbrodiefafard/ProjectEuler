from math import isqrt

import numpy as np

from solutions.SolutionBase import SolutionBase
from util.integers import is_square


class Solution100(SolutionBase):
    NUMBER = 100
    VERIFIED_ANSWER = 756872327473

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        """This problem boils down to: when is 8*(n^2) - 8*n + 1 = m^2. where m^2 is
        a perfect square.
        I can solve this by computing the next term in the diaphonese pair
        equation n_(k+1) = x_1 * n_k + x_2 * m_k + x_3
        equation m_(k+1) = x_1 * n_k + x_2 * m_k + x_3
        These systems have 3 unknowns so we need 3 sample plus 1 for the base
        case. Two of the equations are given and the next 2 I will brute force
        """
        n, m = (15, 85), (41, 239)
        k = n[-1] + 1  # Start searching directly after the second known.
        while len(n) < 4:
            # Compute the square root of the polynomials
            g_square = (8 * (k ** 2) - 8 * k + 1)
            if is_square(g_square):  # Check if integer
                # found one!
                n += (k, )
                m += (isqrt(g_square), )
            k += 1
        # Build and solve the system
        matrix = np.array((n[:3], m[:3], (1, 1, 1))).T
        nx, mx = np.round(np.linalg.solve(matrix, n[1:])), np.round(np.linalg.solve(matrix, m[1:]))
        nk, mk = n[-1], m[-1]
        limit = 10 ** 12
        while True:
            total = (mk + 1) // 2
            if total > limit:
                return nk
            # noinspection PyTypeChecker
            nk, mk = round(np.dot((nk, mk, 1), nx)), round(np.dot((nk, mk, 1), mx))


if __name__ == '__main__':
    Solution100().print_answer()
