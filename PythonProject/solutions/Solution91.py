from itertools import combinations
from math import isclose, ceil, gcd

from solutions.SolutionBase import SolutionBase


class P91(SolutionBase):
    NUMBER = 91
    VERIFIED_ANSWER = 14234

    def run_tests(self, test_case):
        test_case.assertEqual(3, len(list(self.get_right_angle_triangles(1))))
        test_case.assertEqual(3, self.get_num_right_angle_triangles(1))
        test_case.assertEqual(14, len(list(self.get_right_angle_triangles(2))))
        test_case.assertEqual(14, self.get_num_right_angle_triangles(2))

    def get_answer(self):
        return self.get_num_right_angle_triangles(50)

    @staticmethod
    def get_num_right_angle_triangles(n):
        num_triangles = 0
        if n <= 0:
            return num_triangles

        # Count how many triangles with right-angles touching the boundary lines.
        # Every point along the y-axis (0, 1...n), x-axis (1...n, 0), and right-edge (n, 1...n) makes a right-angled
        # triangle with every other point like this.
        # There are 3 of these lines *
        # (the number of points along these lines * the number of points along the perpendicular line)
        num_triangles += 3 * (n ** 2)

        # consider the line from (0, 0) to (x, y)
        # this line will have the slope of y / x
        # let's now make a right angle from this line
        # (there's actually two ways to make a right angle from this line)
        # 1. going up and to the left and 2. going down and to the right
        # To see how many point these lines intersect, we can use the slope to
        # travel in integer jumps. Because there may be many points along the way,
        # we should reduce the fraction of the slope to the smallest form.
        # E.g., if the slope was 4 / 8, we can reduce this to 1 / 2 and move to other points
        # by going 1 up and 2 left or 1 down and 2 right.

        points = (
            # Don't need to consider the points along the axes because we already counted those.
            (x, y) for x in range(1, n + 1) for y in range(1, n + 1)
        )

        for (x, y) in points:
            # simplify slope fraction. integer division ensures integer steps.
            d = gcd(y, x)
            x_step = x // d
            y_step = y // d
            # Since we have one point at (0, 0), one point at (x, y) and a third point along the perpendicular, each one
            # of these points makes a right-angled triangle.
            # use min because both coordinates need to stay within the grid.
            # count how many points there are on the perpendicular line going up and to the left.
            num_triangles += min((n - x) // y_step, y // x_step)
            # count how many points there are on the perpendicular line going down and to the right.
            num_triangles += min((n - y) // x_step, x // y_step)

        return num_triangles

    @staticmethod
    def get_right_angle_triangles(max_bound):
        if max_bound == 0:
            return
        points = (
            (x, y) for x in range(max_bound + 1) for y in range(max_bound + 1)
            if not (x == 0 and y == 0)
        )

        for (x1, y1), (x2, y2) in combinations(points, 2):
            s1_squared = x1 ** 2 + y1 ** 2
            s2_squared = x2 ** 2 + y2 ** 2
            s3_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
            a_squared, b_squared, c_squared = sorted((s1_squared, s2_squared, s3_squared))
            if isclose(a_squared + b_squared, c_squared):
                yield (0, 0), (x1, y1), (x2, y2)

    @staticmethod
    def rescale(v, min_v, max_v, min_t, max_t):
        return (v - min_v) / (max_v - min_v) * (max_t - min_t) + min_t

    def draw_triangles(self, n, triangles, num_triangles):
        from PIL import Image, ImageDraw

        w, h = 1600, 1600

        img = Image.new('RGB', (w, h), (255, 255, 255, 255))
        draw = ImageDraw.Draw(img)

        points = [(x, y) for x in range(n + 1) for y in range(n + 1)]
        num_along_width = num_along_height = int(ceil(num_triangles ** .5))
        padding = 20
        size = min(
            int((((w - padding) / num_along_width) - padding)),
            int((((h - padding) / num_along_height) - padding))
        )
        x = padding
        y = h
        for i, triangle in enumerate(triangles):
            if i % num_along_width == 0:
                y -= size + padding
                x = padding

            self.draw_grid(draw, x, y, size, points, n)
            self.draw_triangle(draw, x, y, size, triangle, n)
            x += size + padding

        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img.show()
        img.save('t_{}.png'.format(str(n)), 'png')

    def draw_triangle(self, draw, x, y, size, triangle, n):
        color = (255, 0, 255, 255)
        triangle = [
            (x + self.rescale(point[0], 0, n, 0, size), y + self.rescale(point[1], 0, n, 0, size))
            for point in triangle
        ]

        draw.line([triangle[0], triangle[1]], fill=color, width=2)
        draw.line([triangle[1], triangle[2]], fill=color, width=2)
        draw.line([triangle[2], triangle[0]], fill=color, width=2)

    def draw_grid(self, draw, x, y, size, points, n):
        color = 'black'
        draw.line([(x, y), (x, y + size)], fill=color, width=2)
        draw.line([(x, y), (x + size, y)], fill=color, width=2)
        draw.line([(x + size, y + size), (x, y + size)], fill=color, width=2)
        draw.line([(x + size, y + size), (x + size, y)], fill=color, width=2)
        p_size = max(6 // n, 1)
        for point in points:
            xy = [
                (x + self.rescale(point[0], 0, n, 0, size) - p_size,
                 y + self.rescale(point[1], 0, n, 0, size) - p_size),
                (x + self.rescale(point[0], 0, n, 0, size) + p_size,
                 y + self.rescale(point[1], 0, n, 0, size) + p_size)]
            draw.arc(xy, 0, 360, fill='black', width=10)

    def draw(self):
        for n in range(1, 4 + 1):
            triangles = self.get_right_angle_triangles(n)
            num_triangles = self.get_num_right_angle_triangles(n)
            self.draw_triangles(n, triangles, num_triangles)


if __name__ == '__main__':
    P91().print_answer()
