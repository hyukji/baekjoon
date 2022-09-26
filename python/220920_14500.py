n, m = map(int, input().split())
paper = []
for i in range(n):
    row = list(map(int, input().split()))
    paper.append(row)

res = []
def dfs(now, cnt, before=None, v=0):
    if cnt == 3:
        res.append(v)
        # print(now, cnt, before, v, res)
        return
    # print(now, cnt, before, v, res)
    route = [[0,1], [1,0], [-1,0]]
    for move in list(map(lambda x: (now[0]+x[0], now[1]+x[1]), route)):
        if 0 <= move[0] < n and 0 <= move[1] < m and move != before:
            dfs(move, cnt +1, now, v + paper[move[0]][move[1]])

def extra(now,v):
    route = [[0,1], [1,0], [-1,0], [0,-1]]
    if 0 < now[0] < n-1 and 0 < now[1] < m-1:
        cross_v = list(map(lambda x: paper[now[0]+x[0]][now[1]+x[1]], route))
        for move_v in cross_v:
            res.append(sum(cross_v) - move_v + v)

for i in range(n):
    for j in range(m):
        dfs((i, j), 0, None, paper[i][j])
        extra([i, j], paper[i][j])
        res = [max(res)]    
        # print(res)
        # print()
    res = [max(res)]    

print(res[0])

#에러

'''
import sys; input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)
'''