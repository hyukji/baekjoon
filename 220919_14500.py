from shutil import move


n, m = map(int, input().split())
paper = []
for i in range(n):
    row = list(map(int, input().split()))
    paper.append(row)

res = []
def dfs(now, cnt, before=None, v=0):
    if cnt == 3:
        res.append(v + paper[now[0]][now[1]])
        return
    route = [[0,1], [1,0], [-1,0]]
    for move in list(map(lambda x: (now[0]+x[0], now[1]+x[1]), route)):
        if 0 <= move[0] < n and 0 <= move[1] < m and move != before:
            # print(move, cnt)
            dfs(move, cnt +1, now, v + paper[now[0]][now[1]])

def extra(now,v):
    route = [[0,1], [1,0], [-1,0], [0,-1]]
    if 0 < now[0] < n-1 and 0 < now[1] < m-1:
        cross_v = list(map(lambda x: paper[now[0]+x[0]][now[1]+x[1]], route))
        for move_v in cross_v:
            res.append(sum(cross_v) - move_v + v)

for i in range(n):
    for j in range(m):
        dfs([i, j], 0)
        extra([i, j], paper[i][j])
        
    res = [max(res)]    

print(res[0])