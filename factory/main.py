from random import triangular
from ShapeFactory import ShapeFactory

circle = ShapeFactory.getShape('circle')
circle.buildRadius(10)
circle.calculateArea()
circle.drawArea()

triangle = ShapeFactory.getShape('triangle')
triangle.buildSideA(3)
triangle.buildSideB(4)
triangle.buildSideC(5)
triangle.calculateArea()