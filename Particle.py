class Particle(object):

    instances = []

    def __init__(self, name="Unnamed", x=0, y=0, x_vel=0, y_vel=0, mass = 1):
        Particle.instances.append(self)
        
        self.name = name

        self.x = x
        self.y = y

        self.x_vel = x_vel
        self.y_vel = y_vel

        self.mass = mass
    
    def display(self):
        print(f"Particle {self.name} is at coordinates ({self.x}, {self.y})")
    
    def move(self, x, y):
        self.x += x
        self.y += y
    
    def checkCollision(self, collider):
        if self.x == collider.x and self.y == collider.y:
            return True
    
    def physicsUpdate(self):
        self.move(self.x_vel, self.y_vel)
        
        collided = False
        for particle in Particle.instances:
            if self.checkCollision(particle):
                total_mass = self.mass + particle.mass
                total_velocity = self.x_vel + self.y_vel + particle.x_vel + particle.y_vel
                total_momentum = total_mass * total_velocity
            
if __name__ == "main":
    a = Particle("Alpha")
    b = Particle("Beta")

