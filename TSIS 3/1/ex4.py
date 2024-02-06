import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Координаты точки: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

# Пример использования класса Point
if __name__ == "__main__":
    point1 = Point(1, 2)
    point2 = Point(4, 6)

    point1.show()  # Выведет: Координаты точки: (1, 2)
    point2.show()  # Выведет: Координаты точки: (4, 6)

    distance = point1.dist(point2)
    print(f"Расстояние между точками: {distance}")  # Выведет: Расстояние между точками: 5.0

    point1.move(3, 5)
    point1.show()  # Выведет: Координаты точки: (3, 5)
