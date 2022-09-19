from itertools import count

n, s = map(int, input().split())
lst = list(map(int, input().split()))

semi_res = [0]
for a in lst:
    update_res = list(map(lambda x: a + x, semi_res))
    semi_res += update_res


semi_res.remove(0)
print(semi_res.count(s))