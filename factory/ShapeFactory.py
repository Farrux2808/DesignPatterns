import shapes


class ShapeFactory():
    def getShape(shapeType):
        if shapeType == 'circle':
            return shapes.Circle()
        elif shapeType == 'triangle':
            return shapes.Triangle()
        else:
            return None