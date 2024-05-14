class Color:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        print("Фигура түсі:", self.color)

class Triangle(Color):
    def __init__(self, color, side1, side2, side3):
        Color.__init__(self,color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.a = side1 + side2 + side3

    def get_perimeter(self):
        print("Perimeter:", self.a)

obj1 = Triangle(color="White", side1=7, side2=3, side3=4)
obj1.get_color()
obj1.get_perimeter()