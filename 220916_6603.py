#dfs # *argv 주소아님ㅎ

def dfs(comb = []):
    depth = len(comb)
    start = 0 if depth == 0 else comb[-1] + 1

    for num in range(start, k-5+depth):
        if depth == 5:
            for i in comb:
                print(s[i], end = ' ')
            print(s[num])
            continue

        dfs(comb[:] + [num])

while True:
    lst = list(map(int, input().split()))
    k = lst[0]
    if k == 0:
        break

    s = lst[1:]
    dfs()
    print()