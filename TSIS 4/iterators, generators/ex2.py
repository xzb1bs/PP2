def even(N):
    for i in range(0, N+1):
        if i%2==0:
            yield(i)

N = int(input())
generator = even(N)

for i in generator:
    print(','.join(map(str, generator)))