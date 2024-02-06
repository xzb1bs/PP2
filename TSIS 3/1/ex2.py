class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

# Пример использования классов
if __name__ == "__main__":
    shape = Shape()
    square = Square(4)

    print("Площадь фигуры (Shape):", shape.area())  # Выведет 0
    print("Площадь квадрата (Square):", square.area())  # Выведет 16
