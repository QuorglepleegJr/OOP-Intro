class Velocity(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # Define basic operations for velocities

    def __add__(a, b):
        return Velocity(a.x_vel + b.x_vel, a.y_vel + b.y_vel)
    