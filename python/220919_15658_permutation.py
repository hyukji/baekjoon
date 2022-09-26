import itertools


n = int(input())
a = list(map(int, input().split()))
opts = list(map(int, input().split()))

refined_opts = []
for i in range(4):
    refined_opts += [i for _ in range(opts[i])]

P_opts = list(set(itertools.permutations(refined_opts)))

min_res = 10**9
max_res = 10**9*(-1)

for p in P_opts:
    l = a[0]
    for rp in zip(a[1:],p):
        if rp[1] == 0:
            l += rp[0]
        elif rp[1] == 1:
            l -= rp[0]
        elif rp[1] == 2:
            l *= rp[0]
        elif rp[1] == 3: 
            l = int(l / rp[0])

    if l < min_res:
        min_res = l
    if l > max_res:
        max_res = l

print(max_res, min_res)