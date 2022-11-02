from Vector import Vector
from math import pi

class Particle(object):

    # Static Variables

    __instances = []

    # Static Functions

    def __getCollisions():
        collisions = []
        particles = list(Particle.__instances)
        max_len = len(particles)
        for index1 in range(max_len-1): # Obtain all pairs of particles
            for index2 in range(index1+1, max_len):
                part_a = particles[index1]
                part_b = particles[index2]
                if part_a.__pos == part_b.__pos:
                    collisions.append((part_a, part_b))
        return collisions

    # Static Procedures

    def __handleCollisions():
        for part_a, part_b in Particle.__getCollisions(): # Formulae found online at http://hyperphysics.phy-astr.gsu.edu/hbase/elacol2.html#c3
            frame_of_reference_modifier = part_b.__vel * -1 # To be added to give a frame of reference with b at rest
            m1 = part_a.__mass
            m2 = part_b.__mass
            relative_a_vel = part_a.__vel + frame_of_reference_modifier
            vel_b = relative_a_vel * ((2*m1)/(m1+m2))
            vel_a = relative_a_vel * ((m1-m2)/(m1+m2))
            part_a.__vel = vel_a - frame_of_reference_modifier
            part_b.__vel = vel_b - frame_of_reference_modifier

    def updateAll():
        for particle in Particle.__instances:
            particle.__update()
        Particle.__handleCollisions()

    # Constructor

    def __init__(self, name="Unnamed", x=0, y=0, x_vel=0, y_vel=0, mass=1):
        Particle.__instances.append(self)
        
        self.name = name

        self.__pos = Vector(x, y)

        self.__vel = Vector(x_vel, y_vel)

        self.__mass = mass
    
    # Procedures

    def display(self):
        print(f"Particle {self.name} is at coordinates {self.pos}, with velocity {self.vel}")
    
    def __move(self, vel):
        self.__pos += vel
    
    def __update(self):
        self.__move(self.__vel)
        self.display()
                

class Wall(object):

    # Static Methods
    def allCollideParticles():
        pass

    def collideParticles(self):
        pass

#if __name__ == "main":
from time import sleep

a = Particle("Alpha", x=1, x_vel=-1)
b = Particle("Beta", x=-1, x_vel=1)


for x in range(10):
    Particle.updateAll()
    sleep(0.5)