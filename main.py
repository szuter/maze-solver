from graphics import *


def main():
    win = Window(800, 600)
    line = Line(Point(10, 10), Point(100, 100))
    win.draw_line(line, "black")
    win.wait_for_close()


main()
