from interfaces import IShape

class Rectangel(IShape):
    
    def calculateArea(self):
        self.area = self.sideA * self.sideB
        print(f"This rectangel are equal = {self.area}")

    def drawArea(self):
        print(f"This rectangel drawen. Side a = {self.sideA} b = {self.sideB}")
