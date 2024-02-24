def div(N):
    for i in range(0, N+1):
        if i%3==0 and i%4==0:
            yield i

N = int(input())
generator = div(N)
for i in generator:
    print(i)