from math import sqrt, acos, cos, sin
class Vector(object):
    def fromAngle(m=0, a=0):
        x = m*cos(a)
        y = m*sin(a)
        return Vector(x,y)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # Define basic operations for velocities

    def __add__(a, b):
        if isinstance(b, Vector):
            return Vector(a.x_vel + b.x_vel, a.y_vel + b.y_vel)
        return NotImplemented
    
    def __mul__(a, b):
        if isinstance(b, Vector):
            return a.x * b.x + a.y * b.y
        elif isinstance(b, int):
            return Vector(a.x * b, a.y * b)
        return NotImplemented
    
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def findAngle(self, vec):
        return acos((self*vec)/(abs(self)*abs(vec)))
    
