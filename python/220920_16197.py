n, m = map(int, input().split())
board = []
loc = [[]]
for i in range(n):
    row = list(input())
    board.append(row)
    
    for j in range(m):
        if row[j] == "o":
            loc[0].append([i, j])


route = [[0,1],[1,0],[-1,0],[0,-1]]

def bfs(before_c, cnt = 0):
    if cnt == 10:
        print(-1)
        return
    cnt += 1
    new_c = []
    for move in route:
        for c in before_c:
            c1 = [c[0][0]+move[0], c[0][1]+move[1]]
            c2 = [c[1][0]+move[0], c[1][1]+move[1]]

            if 0 <= c1[0] < n and 0<= c1[1] < m and 0 <= c2[0] < n and 0<= c2[1] < m:
                if board[c1[0]][c1[1]] == "#": #c1이벽에
                    c1 = c[0]
                if board[c2[0]][c2[1]] == "#": #c2도 벽에
                    c2 = c[1]
                
                if c1 == c2:
                    continue
                else:
                    if [c1,c2] in before_c or [c1,c2] in new_c:
                        continue
                    new_c.append([c1,c2])

            elif 0 <= c1[0] < n and 0<= c1[1] < m: #c1은 안 떨어졌을 때
                print(cnt)
                return
            elif 0 <= c2[0] < n and 0<= c2[1] < m: #c2는 안 떨어졌을 때
                print(cnt)
                return
                
            
    bfs(new_c, cnt)

bfs(loc)