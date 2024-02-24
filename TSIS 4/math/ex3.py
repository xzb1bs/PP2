import math

def polygon_area(n, a):
    area = (n * a**2 ) / (4 * math.tan(math.pi / n))
    return area

n = int(input())
a = int(input())

area = polygon_area(n, a)
print(area)