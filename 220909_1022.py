r1,c1,r2,c2 = map(int, input().split())
res = []
max_len = 0
for r in range(r1, r2+1):
    semi_res = []
    for c in range(c1, c2+1):
        v = 0
        i = max(abs(r), abs(c))
        if r < c:
            v = 4*i*i+1-(2*i+r+c)
        else:
            v= 4*i*i+1+(2*i+r+c)
        semi_res.append(str(v))
        if len(semi_res[-1]) > max_len:
            max_len = len(semi_res[-1])

    res.append(semi_res)
        
for r in res:
    line = ""
    for v in r:
        line += " " * (max_len - len(v)) + v + " "
    print(line[:-1])

