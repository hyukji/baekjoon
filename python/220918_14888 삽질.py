n = int(input())
a = list(map(int, input().split()))
opts = list(map(int, input().split()))

def calc(l,r,opt):
    if opt == 0:
        return l + r
    elif opt == 1:
        return l - r
    elif opt == 2:
        return l * r
    elif opt == 3: 
        return int(l / r)


def dfs(v, now_a, now_opts):
    res = []
    for r in now_a:
        new_a = now_a[:]
        new_a.remove(r)
        
        for opt in range(4):
            if now_opts[opt]:
                new_opts = now_opts[:]
                new_opts[opt] -= 1

                new_v = calc(v, r, opt)
                # print(new_v, v, r, opt, now_a, now_opts)

                if not len(new_a):
                    # print(new_v)
                    return [new_v]
                res += dfs(new_v, new_a, new_opts)

    # print(len(a) - len(now_a), res)
    # return [min(res), max(res)]
    return res

res = []

for i in a:
    new_a = a[:]
    new_a.remove(i)
    # print(i, new_a, opts)
    # print()
    res += dfs(i, new_a, opts)

print(set(res))
print(max(res), min(res))


