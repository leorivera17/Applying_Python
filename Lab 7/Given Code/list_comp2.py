# Lab 7
# Section 3
# S. Einakian
# Tommy Pho

from objects import *


def distance_all(list1):
    newL = list(map(distance,list1))
    return newL


def quadrant(point1):
    if point1.x > 0 and point1.y > 0:
        return True
    return False


def are_in_first_quadrant(list1):
    newL = list(filter(quadrant, list1))
    return newL


def circle_distance_all(circlelist):
    alist = [circlelist[x].center for x in range(len(circlelist))]
    Jlist = [distance_all(alist)[x] for x in range(len(circlelist))]
    return Jlist


def overlaps_all(circlelist):
    UnitC = Circle(Point(0, 0), 1)
    Jlist = [circlelist[i] for i in range(len(circlelist)) if overlaps(UnitC, circlelist[i])]
    return Jlist