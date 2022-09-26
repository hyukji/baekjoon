N, K = map(int, input().split())

i = 0
bought_bottle = 0
made_bottle = []
while True:
    if 2**(i) > N:
        made_bottle.append(2**(i-1)) 
        N -= 2**(i-1)
        i = 0   
        continue
    elif 2**(i) == N:
        made_bottle.append(2**(i)) 
        N = sum(made_bottle)
        break

    i += 1

if K >= len(made_bottle):
    print(0)
else:
    print(made_bottle[K-1] - sum(made_bottle[K:]))

