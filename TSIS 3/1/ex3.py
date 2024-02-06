class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Пример использования класса Rectangle
if __name__ == "__main__":
    rectangle = Rectangle(5, 3)

    print("Площадь прямоугольника:", rectangle.area())  # Выведет 15
