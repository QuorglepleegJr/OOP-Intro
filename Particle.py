from Vector import Vector
from math import pi

class Particle(object):

    # Static Variables

    instances = []

    # Static Functions

    def getCollisions():
        collisions = []
        particles = list(Particle.instances)
        max_len = len(particles)
        for index1 in range(max_len - 2): # Obtain all pairs of particles
            for index2 in range(index1+1, max_len-1):
                part_a = particles[index1]
                part_b = particles[index2]
                if part_a.pos == part_b.pos:
                    collisions.append((part_a, part_b))
        return collisions

    # Static Procedures

    def handleCollisions():
        for part_a, part_b in Particle.getCollisions():
            print(f"Collision between {part_a.name} and {part_b.name}: ({part_a.pos}) & ({part_b.pos})")

    # Constructor

    def __init__(self, name="Unnamed", x=0, y=0, x_vel=0, y_vel=0, mass=1):
        Particle.instances.append(self)
        
        self.name = name

        self.pos = Vector(x, y)

        self.vel = Vector(x_vel, y_vel)

        self.mass = mass

        self.momentum = self.vel * self.mass
        self.energy = 0.5 * self.mass * abs(self.vel)**2
    
    # Attribute getsets

    def getMomentum(self):
        return self.momentum
    
    def getEnergy(self):
        return 0.5 * self.mass * abs(self.vel)**2
    
    # Procedures

    def display(self):
        print(f"Particle {self.name} is at coordinates ({self.x}, {self.y}), with velocity {self.vel}")
    
    def move(self, vel):
        self.pos += vel
    
    def update(self):
        self.move(self.vel)
        self.momentum = self.vel * self.mass
        self.energy = 0.5 * self.mass * abs(self.vel)**2
        self.display()
        
    
    #def collisionUpdate(self):
    #    for particle in Particle.instances:
    #        if particle is not self:
    #            if self.checkCollision(particle):
    #                self_momentum_mag = abs(self.vel * self.mass)
    #                other_momentum_mag = abs(particle.vel_before_collision * particle.mass)
    #                total_momentum_mag = self_momentum_mag + other_momentum_mag
    #                new_angle = pi + self.vel.findAngle() - self.vel.findAngle(particle.vel_before_collision)
    #                new_magnitude = total_momentum_mag*self.mass/(self.mass + particle.mass)
    #                print(f"{self.name} colliding with {particle.name}:", round(10000*new_angle/pi)/10000, round(10000*self.vel.findAngle()/pi)/10000, round(10000*self.vel.findAngle(particle.vel_before_collision)/pi)/10000)
    #                self.vel = Vector.fromAngle(new_magnitude, new_angle)
                
            
#if __name__ == "main":
from time import sleep

a = Particle("Alpha", x=-1, y=-1, x_vel=1, y_vel=1)
b = Particle("Beta", x=1, y=-1, x_vel=-1, y_vel=1)


while True:
    for particle in Particle.instances:
        particle.update()
    Particle.handleCollisions()
    sleep(0.5)