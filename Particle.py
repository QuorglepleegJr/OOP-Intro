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
        for index1 in range(max_len-1): # Obtain all pairs of particles
            for index2 in range(index1+1, max_len):
                part_a = particles[index1]
                part_b = particles[index2]
                if part_a.pos == part_b.pos:
                    collisions.append((part_a, part_b))
        return collisions

    # Static Procedures

    def handleCollisions():
        for part_a, part_b in Particle.getCollisions(): # Formulae found online at http://hyperphysics.phy-astr.gsu.edu/hbase/elacol2.html#c3
            frame_of_reference_modifier = part_b.vel * -1 # To be added to give a frame of reference with b at rest
            m1 = part_a.mass
            m2 = part_b.mass
            relative_a_vel = part_a.vel + frame_of_reference_modifier
            vel_b = relative_a_vel * ((2*m1)/(m1+m2))
            vel_a = relative_a_vel * ((m1-m2)/(m1+m2))
            part_a.vel = vel_a - frame_of_reference_modifier
            part_b.vel = vel_b - frame_of_reference_modifier

    def updateAll():
        for particle in Particle.instances:
            particle.update()
        Particle.handleCollisions()

    # Constructor

    def __init__(self, name="Unnamed", x=0, y=0, x_vel=0, y_vel=0, mass=1):
        Particle.instances.append(self)
        
        self.name = name

        self.pos = Vector(x, y)

        self.vel = Vector(x_vel, y_vel)

        self.mass = mass

        self.momentum = self.vel * self.mass
        self.energy = 0.5 * self.mass * abs(self.vel)**2
    
    # Procedures

    def display(self):
        print(f"Particle {self.name} is at coordinates {self.pos}, with velocity {self.vel}")
    
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

a = Particle("Alpha", x=1, x_vel=-1)
b = Particle("Beta", x=-1, x_vel=1)


for x in range(10):
    Particle.updateAll()
    sleep(0.5)