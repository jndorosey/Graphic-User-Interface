import math
from template import Point, Template


class Recognizer:
    def __init__(self, templates):
        # self.templates = templates
        self.templates = templates

    def recognize(self, points, n=32):
        """Recognizer main function.

        Match points against a set of templates by employing the Nearest-Neighbor classification rule.

        Parameters
        ----------
        points:
            List of Point objects.
        n:
            Number of resampled points per gesture.

        Returns
        -------
        result[:5]  # return the first five recognized word candidates if gesture has more than 2 points

        """

        result = []
        points = self._normalize(points, n)
        score = float("inf")


        for t in range(len(self.templates)):
            template = self._normalize(self.templates[t], n)
            d = self._distance_match(points, template, n)
            result.append([d, template.name, t])

            '''
            if score > d:
                score = d
                result = template
            '''
        result.sort() # sort according to d in result
        if len(points) > 1:  # more than 2 points in the gesture
            return result[:5]  # return the first five candidates
        else:
            return []  # return null

    def _distance_match(self, points, template, n):
        d = [self._euclidean_distance(x, y) for x, y in zip(points, template)]  # [a[i]+b[i] for i in range(len(a))]
        return sum(d)

    def _euclidean_distance(self, point_1, point_2):
        return math.hypot(point_1.x - point_2.x,
                          point_1.y - point_2.y)

    def _normalize(self, points, n):  # for the gesture keyboard, just resample and translate
        if len(points) > 1:  # more than 2 points in the gesture
            points = self._resample(points, n)
            # points = self._scale(points)
            points = self._translate_to_origin(points, n)
        return points

    def _resample(self, points, n):
        I = self._path_length(points) / (n - 1)
        D = 0
        if isinstance(points, Template):
            new_points = Template(points.name, [points[0]])
        else:
            new_points = [points[0]]

        i = 1
        while True:
            d = self._euclidean_distance(points[i - 1], points[i])
            if D + d >= I:
                q = Point(points[i - 1].x + ((I - D) / d) * (points[i].x - points[i - 1].x),
                          points[i - 1].y + ((I - D) / d) * (points[i].y - points[i - 1].y))
                new_points.append(q)
                points.insert(i, q)
                D = 0
            else:
                D += d

            i += 1
            if i == len(points):
                break
        if len(new_points) == n - 1:
            p = points[-1]
            new_points.append(Point(p.x, p.y))
        return new_points

    def _path_length(self, points):
        d = 0

        for i in range(1, len(points)):
            d += self._euclidean_distance(points[i - 1], points[i])
        return d

    def _scale(self, points):
        x_min = float("inf")
        x_max = 0
        y_min = float("inf")
        y_max = 0

        if isinstance(points, Template):
            new_points = Template(points.name, [])
        else:
            new_points = []

        for p in points:
            x_min = min(x_min, p.x)
            x_max = max(x_max, p.x)
            y_min = min(y_min, p.y)
            y_max = max(y_max, p.y)
        scale = max(x_max - x_min, y_max - y_min)

        for p in points:
            q = Point((p.x - x_min) / scale,
                      (p.y - y_min) / scale)
            new_points.append(q)
        return new_points

    def _translate_to_origin(self, points, n):
        if isinstance(points, Template):
            new_points = Template(points.name, [])
        else:
            new_points = []

        x = 0
        y = 0
        for p in points:
            x += p.x
            y += p.y
        x /= n
        y /= n

        for p in points:
            q = Point((p.x - x),
                      (p.y - y))
            new_points.append(q)
        return new_points
