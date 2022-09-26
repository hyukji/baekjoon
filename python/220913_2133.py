N = int(input())
if N % 2 == 0:
    N = N//2
    p = [0 for _ in range(N+1)]
    p[0] = 1
    p[1] = 3

    for i in range(2,N+1):
        p[i] = 3*p[i-1] +2*sum(p[0:i-1])
        
    print(p[-1])

else:
    print(0)