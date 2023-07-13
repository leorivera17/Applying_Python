# Lab 7
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3


from objects import *


# purpose- to find the distance between two given lines
def distance_all(list1: list) -> list:
    return [point.distance(Point(0, 0)) for point in list1]


# purpose- this function returns true or false
def are_in_first_quadrant(list1: list) -> list:
    return [point for point in list1 if point.x_cord > 0 and point.y_cord > 0]


# purpose- this functions finds the distance between 2 circles
def circle_distance_all(circle_list):
    return [circle.center.distance(Point(0, 0)) for circle in circle_list]


# purpose- this function finds/see if 2 circles overlap
def overlaps_all(circle_list):
    return [circle for circle in circle_list if circle.overlaps(Circle(Point(0, 0), 1))]
