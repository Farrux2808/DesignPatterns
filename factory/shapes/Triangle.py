import interfaces
from math import sqrt

class Triangle(interfaces.IShape):
    def buildSideA(self, sideA):
        self.sideA = sideA
        return self

    def buildSideB(self, sideB):
        self.sideB = sideB
        return self
    
    def buildSideC(self, sideC):
        self.sideC = sideC
        return self

    def getSideA(self):
        return self.sideA
    
    def getSideB(self):
        return self.sideB

    def getSideC(self):
        return self.sideC
    
    def calculateArea(self):
        self.perimeter = self.sideA + self.sideB + self.sideC
        p = self.perimeter / 2
        self.area = sqrt(p * (p - self.sideA) * (p - self.sideB) * (p - self.sideC))
        print(f"This triangle are equal = {self.area}")

    def drawArea(self):
        print(f"This triangle drawen. Side a = {self.sideA} b = {self.sideB} c = {self.sideC}")
