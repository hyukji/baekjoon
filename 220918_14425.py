N = int(input())
s = list(map(int, input().split()))
s.sort()

semi_res = {0}
for a in s:
    new_res = set(map(lambda x: a+x, semi_res))

    semi_res = semi_res | new_res
    cont = set(range(max(semi_res) + 1))
    
    if len(cont - semi_res)  > 0:
        print(min(cont - semi_res))
        break
else:
    print(max(semi_res) + 1)