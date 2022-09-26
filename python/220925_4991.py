from collections import deque
from math import inf

while True:
    c, r = map(int, input().split())
    if c == 0 and r == 0:
        break
    room = []
    dirty = []
    for i in range(r):
        row = list(input())
        room.append(row)
        loc = 0
        while True:
            if loc < c and "*" in row[loc:]:
                loc = row.index("*", loc)
                dirty.append((i, loc))
                loc += 1
                continue
            break

        if "o" in row:
            start = (i, row.index("o"))
    dirty = [start] + dirty

    def bfs(gr, now): # 두 점 사이의 최소거리
        res = [-1 if i > gr else 0 for i in range(n_dirty) ]

        visited = [[0] * c for _ in range(r)]
        visited[now[0]][now[1]] = 1

        dq = deque([now])
        route = [(0,1),(0,-1),(-1,0),(1,0)]

        cnt = 1
        while True:
            if len(dq) == 0 or -1 not in res:
                return res

            for _ in range(len(dq)):
                lr, lc = dq.popleft()
                for move in route:
                    nr = lr + move[0]
                    nc = lc + move[1]
                    if 0 <= nr < r and 0 <= nc < c and visited[nr][nc] == 0:
                        if room[nr][nc] == 'x':
                            continue
                        else:
                            dq.append((nr, nc))
                            visited[nr][nc] += 1
                            if room[nr][nc] == '*':
                                dirty_index = dirty.index((nr, nc))
                                res[dirty_index] = cnt

            cnt += 1


    def tsp(cur, visited):
        if visited == (2**n_dirty -1):
            return 0
        if dp[cur][visited] != 0:
            return dp[cur][visited]
            
        dp[cur][visited] = inf
        for next in range(1, n_dirty):
            if visited != (visited | (1 << next)): #방문한 적이 없다면
                dist = graph[cur][next] if cur < next else graph[next][cur]
                dp[cur][visited] = min(dp[cur][visited], tsp(next, visited | (1 << next)) + dist)

        return dp[cur][visited]



    n_dirty = len(dirty)
    graph = [[0] * n_dirty for _ in range(n_dirty)]
    for gr in range(n_dirty-1):
        graph[gr] = bfs(gr, dirty[gr])
        if -1 in graph[gr]:
            print(-1)
            break
    else:
        dp = [[0] * (2**n_dirty) for _ in range(n_dirty)]
        print(tsp(0, 1))



