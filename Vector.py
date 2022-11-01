from math import sqrt, acos, cos, sin
class Vector(object):
    def fromAngle(m=0, a=0):
        x = round(m*cos(a)*10000)/10000 # Removes most floating-point error
        y = round(m*sin(a)*10000)/10000
        return Vector(x,y)

    def __init__(self, x=0, y=0, copy_vec=None):
        if copy_vec is None:
            self.x = x
            self.y = y
        else:
            self.x = copy_vec.x
            self.y = copy_vec.y
    
    # Overloading base operations

    def __eq__(a, b):
        return a.x == b.x and a.y == b.y

    def __add__(a, b):
        if isinstance(b, Vector):
            return Vector(a.x + b.x, a.y + b.y)

    def __sub__(a, b):
        return Vector(a.x - b.x, a.y - b.y)
    
    def __mul__(a, b):
        if isinstance(b, Vector):
            return a.x * b.x + a.y * b.y
        return Vector(a.x * b, a.y * b)
    
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def findAngle(self, vec=None):
        if vec is None:
            vec = Vector(1,0)
        if abs(vec) != 0:
            return acos((self*vec)/(abs(self)*abs(vec)))
        return 0