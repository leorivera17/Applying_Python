# Lab 7
# Section 3
# S. Einakian
# Tommy Pho
from math import* 
# point class
class Point:

    def __init__(self, xcoor, ycoor):
        self.x = xcoor
        self.y = ycoor

    def __eq__(self, other):
        return type(self) == type(other) and \
               self.x == other.x and \
               self.y == other.y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)


def distance(point1, point2 = Point(0,0)):
    dist = sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)
    return dist


# circle class
class Circle:

    def __init__(self, centPoint, radius):
        self.center = centPoint
        self.r = radius

    def __eq__(self, other):
        return type(self) == type(other) and \
               self.center.x == other.center.x and \
               self.center.y == other.center.y and \
               self.r == other.r

    #def __ne__(self, other):
    #    return True

    def __repr__(self):
        return 'center: {}, radius: {:.2f}'.format(self.center, self.r)


def overlaps(circle1, circle2):
    dist = distance(circle1.center, circle2.center)
    sum = circle1.r + circle2.r
    return dist < sum
