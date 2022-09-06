M, N = map(int, input().split())
locs = list(map(int, input().split()))

sum_opt = 0

locs = [x-1 for x in locs]
for _ in range(len(locs)):
    loc = locs.pop(0)
    opt = 0

    if loc <= M // 2: #2번
        opt = loc
        locs = [x-opt if x-opt >=0 else x-opt+M for x in locs]
    else: #3번
        opt = M-loc
        locs = [x+opt if x+opt < M else x+opt-M for x in locs]

    #1번
    M -= 1
    locs = [x-1 for x in locs]

    sum_opt += opt

print(sum_opt)




    


