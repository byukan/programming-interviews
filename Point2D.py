"""
    @file Point2D.py
    @brief Point 2D class
"""


# Point 2D class and ccw member function
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def ccw(a, b, c):
        area2 = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)  # (b-a)x(c-a)
        if area2 > 0:  # ccw
            return 1
        elif area2 < 0:  # cw
            return -1
        else:  # collinear
            return 0


a = Point2D(2, 4)
b = Point2D(1, 2)
c = Point2D(0, 1)

print(Point2D.ccw(a, b, c))
