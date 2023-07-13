# Lab 7
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3

import math


class Point:

    # Purpose- To make a coordinate system
    def __init__(self, x: int, y: int):
        self.x_cord = x
        self.y_cord = y

    # Purpose- this function makes the other value equal to the old one
    def __eq__(self, other) -> bool:
        return type(self) == type(other) == Point and self.x_cord == other.x_cord and self.y_cord == other.y_cord

    # Purpose- this function prints or represents the value
    def __repr__(self) -> str:
        return 'Point(' + str(self.x_cord) + ', ' + str(self.y_cord) + ')'

    # Purpose- this is the function to calculate the distance of 2 points
    # Point Point -> float
    def distance(self, point2):
        dist = math.sqrt((point2.x_cord - self.x_cord) ** 2 + (point2.y_cord - self.y_cord) ** 2)
        return dist


class Circle:

    # Purpose- this function creates a 'circle'
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    # Purpose- this function gets a new value and equals it to the old one
    def __eq__(self, other) -> bool:
        return type(self) == type(other) and \
               self.center.x_cord == other.center.x_cord and \
               self.center.y_cord == other.center.y_cord and \
               self.radius == other.radius

    # Purpose- this valeu gets the new vaule and makes sure it doesn't equal the old one
    def __ne__(self, other) -> bool:
        return type(self) == type(other) and \
               self.center.x_cord != other.center.x_cord and \
               self.center.y_cord != other.center.y_cord and \
               self.radius != other.radius

    # Purpose- this function check if 2 circles overlap
    # Point, Point -> float
    def overlaps(self, circle2):
        dis = self.center.distance(circle2.center)
        res = self.radius + circle2.radius
        return dis < res
