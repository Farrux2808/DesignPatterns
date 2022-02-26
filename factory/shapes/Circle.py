import interfaces
from math import pi

class Circle(interfaces.IShape):
    def buildRadius(self, radius):
        self.raduis = radius
        return self
    
    def getRadius(self):
        return self.radius
    
    def calculateArea(self):
        self.area = pi * self.raduis ** 2
        print(f"This rectangel are equal = {self.area}")

    def drawArea(self):
        print(f"This rectangel drawen. Radius r = {self.raduis}")
