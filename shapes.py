import shapes

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return 2 * (self.length + self.width)

    def perimeter(self):
        pass

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

if __name__ == "__main__":
    rect = shapes.Rectangle(2, 4)
    print(rect.area())
    square = Square(8)
    print(square.area())
    print(square.perimeter())