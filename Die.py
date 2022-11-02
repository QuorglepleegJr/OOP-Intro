from random import randint
class Die(object):

    # Static Atttributes
    __next_serial = 0

    # Constructor
    def __init__(self, num_faces=6):
        self.__serial = Die.__next_serial
        Die.__next_serial += 1
        self.__num_faces = num_faces
        self.__value = 1
        self.roll()
    
    # Accesors and Mutators
    def getNumFaces(self):
        return self.__num_faces
    
    def getValue(self):
        return self.__value
    
    def setValue(self, value):
        if value in range(1,self.__num_faces + 1):
            self.__value = value
        else:
            try:
                value = int(value) % self.__num_faces
                if value == 0:
                    value += self.__num_faces
                self.__value = value
                raise RuntimeWarning(f"Attempting to set value of Die to inappropriate but handlable data")
            except ValueError:
                raise RuntimeError(f"Attempt to set value of Die to unhandlable inappropriate data")

    def getSerial(self):
        return self.__serial

    # Methods
    def roll(self):
        value = randint(1,self.__num_faces)
        self.value = value
        return value

class DiceSet(object):
    def __init__(self):
        self.__dice = []
    
    def addDie(self, die):
        self.__dice.append(die)
    
    def rollAll(self):
        total = 0
        for die in self.__dice:
            total += die.roll()
        return total
    
    def findTotal(self):
        total = 0
        for die in self.__dice:
            total += die.getValue()
        return total
    
    def debugInfo(self):
        print(self.__dice)
        for die in self.__dice:
            print(die.getValue(),end=", ")
        print()

double6 = DiceSet()
double6.addDie(Die())
double6.addDie(Die())
double6.debugInfo()
print(double6.rollAll())
double6.debugInfo()
print(double6.findTotal())
double6.debugInfo()