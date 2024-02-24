import math

def deg_to_rad(n):
    rad = n * (math.pi / 180)
    return rad

degree = float(input())

radian = deg_to_rad(degree)
print(radian)