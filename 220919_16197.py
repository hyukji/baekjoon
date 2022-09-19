n, m = map(int, input().split())
board = []
loc = []
for i in range(n):
    row = list(input())
    board.append(row)
    
    if "o" in row:
        loc.append([i, row.index("o")])


route = [[0,1],[1,0],[-1,0],[0,-1]]
cnt = 0
def bfs(before_c):
    if cnt == 10:
        print(-1)
    cnt += 1
    new_c = []
    for move in route:
        for c in before_c:
            c1 = [c[0][0]+move[0], c[0][1]+move[1]]
            c2 = [c[1][0]+move[0], c[1][1]+move[1]]

            if c1 == c2:
                continue
            elif 0 <= c1 < n and 0 <= c2 < m:
                if board[c1[0]][c1[1]] == "#":
                    c1 = before_c
                elif board[c2[0]][c2[1]] == "#":
                    continue
            else:
                if not 0 <= c1 < n or 0 <= c2 < m:
                    continue
                print(cnt)
                return

    bfs(new_c)


