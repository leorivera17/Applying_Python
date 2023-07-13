# Lab 7
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3

class Point():

    def __init__(self, x: int, y: int):
        self.x_cord = x
        self.y_cord = y
        if x == y:
            return True
        else:
            return False

    def __eq__(self, other) -> bool:
        return type(self) == type(other) == Point

    def __repr__(self) -> str:
        return 'Point(' + str(self.x_cord) + ', ' + str(self.y_cord) + ')'
