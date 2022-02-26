from abc import abstractmethod


class IShape():

    @abstractmethod
    def calculateArea(self):
        pass

    @abstractmethod
    def drawArea(self):
        pass
