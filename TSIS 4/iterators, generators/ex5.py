def revers(N):
    for i in range(N, -1, -1):
        yield i

N = int(input())
gen = revers(N)
for i in gen:
    print(i)