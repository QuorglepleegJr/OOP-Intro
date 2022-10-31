from math import sqrt, acos
class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # Define basic operations for velocities

    def __add__(a, b):
        return Vector(a.x_vel + b.x_vel, a.y_vel + b.y_vel)
    
    def __mul__(a, b):
        # Dot product
        return a.x * b.x + a.y * b.y
    
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def findAngle(self, vec):
        return acos((self*vec)/(abs(self)*abs(vec)))
