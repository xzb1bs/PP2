def squares(N):
    for i in range(1, N+1):
        yield(i**2)

N = int(input())
squares_generator = squares(N)

for i in squares_generator:
    print(i)



