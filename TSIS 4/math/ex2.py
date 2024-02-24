def trapezoid(n , l , h):
    area = 0.5 * (n+l) * h 
    return area

n = float(input())
l = float(input())
h = float(input())
answer = trapezoid(n , l , h)
print(answer)