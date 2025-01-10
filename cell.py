from graphics import Point, Line


class Cell:
    def __init__(self, window):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

        self._window = window

    def draw(self, x1, y1, x2, y2):
        if self.has_left_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_top_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_right_wall:
            self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)))
