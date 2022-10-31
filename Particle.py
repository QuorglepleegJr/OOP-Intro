from Vector import Vector
from math import pi

class Particle(object):

    instances = []

    def __init__(self, name="Unnamed", x=0, y=0, x_vel=0, y_vel=0, mass=1):
        Particle.instances.append(self)
        
        self.name = name

        self.x = x
        self.y = y

        self.vel = Vector(x_vel, y_vel)

        self.vel_before_collision = Vector(copy_vec=self.vel)

        self.mass = mass
    
    def display(self):
        print(f"Particle {self.name} is at coordinates ({self.x}, {self.y}), with velocity {self.vel}")
    
    def move(self, vel):
        self.x += vel.x
        self.y += vel.y
    
    def checkCollision(self, collider):
        #print(f"Collision check between {self.name} and {collider.name}: ({self.x}, {self.y}) & ({collider.x}, {collider.y}) -> {self.x == collider.x and self.y == collider.y}")
        if self.x == collider.x and self.y == collider.y:
            return True
    
    def collisionUpdate(self):
        for particle in Particle.instances:
            if particle is not self:
                if self.checkCollision(particle):
                    self_momentum_mag = abs(self.vel * self.mass)
                    other_momentum_mag = abs(particle.vel_before_collision * particle.mass)
                    total_momentum_mag = self_momentum_mag + other_momentum_mag
                    new_angle = pi + self.vel.findAngle() - self.vel.findAngle(particle.vel_before_collision)
                    new_magnitude = total_momentum_mag*self.mass/(self.mass + particle.mass)
                    print(f"{self.name} colliding with {particle.name}:", round(10000*new_angle/pi)/10000, round(10000*self.vel.findAngle()/pi)/10000, round(10000*self.vel.findAngle(particle.vel_before_collision)/pi)/10000)
                    self.vel = Vector.fromAngle(new_magnitude, new_angle)
                
            
#if __name__ == "main":
from time import sleep

a = Particle("Alpha", x=-1, y=-1, x_vel=1, y_vel=1)
b = Particle("Beta", x=1, y=-1, x_vel=-1, y_vel=1)


while True:
    for particle in Particle.instances:
        particle.display()
        particle.move(particle.vel)
    for particle in Particle.instances:
        particle.vel_before_collision = Vector(copy_vec=particle.vel)
        particle.collisionUpdate()
    
    sleep(0.5)