"""Demonstrates the use of the Robot class and class inheritance."""

class Robot:
    """Represents a robot with a name."""
    
    def __init__(self,name):
        self.name = name
        self.position=[0,0]
        self.direction='N'
        self.directions=['N','E','S','W']
        print("My name is", self.name)
    
    def walk(self,x,y):
        self.position[0]= x[0]
        self.position[1]= x[1]
        self.direction=y
        print("New position is ",self.position, 'with a heading of', self.direction)

"""A robot dog class that inherits from the Robot class."""
class Robot_Dog(Robot):  #class constructor

    def make_noise(self):
        print("Bark! Bark!")

# main program
my_robot_dog = Robot_Dog("Rover")
my_robot_dog.walk([1,1],'E')
my_robot_dog.make_noise()

