import itertools


n = int(input())
a = list(map(int, input().split()))
opts = list(map(int, input().split()))

refined_opts = []
for i in range(4):
    refined_opts += [i for _ in range(opts[i])]

P_opts = list(set(itertools.permutations(refined_opts)))

def calc(l,r,opt):
    if opt == 0:
        return l + r
    elif opt == 1:
        return l - r
    elif opt == 2:
        return l * r
    elif opt == 3: 
        return int(l / r)

min_res = 10**9
max_res = 10**9*(-1)

for p in P_opts:
    v = a[0]
    for rp in zip(a[1:],p):
        v = calc(v, rp[0], rp[1])
    if v < min_res:
        min_res = v
    if v > max_res:
        max_res = v

print(max_res, min_res)