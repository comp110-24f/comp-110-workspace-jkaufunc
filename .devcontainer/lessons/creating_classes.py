"""CQ09"""


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_length(self) -> float:
        return (
            ((self.end.x - self.start.x) ** 2) + ((self.end.y - self.start.y))
        ) ** 0.5

        """
        or
        x_diffs: float = self.end.x - self.start.x
        y_diffs: float = self.end.y - self.start.y
        return ((x_diffs**2)+(y_diffs**2))**0.5
        """

    def get_slope(self) -> float:
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)
