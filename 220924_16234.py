from collections import deque

n, l, r = map(int, input().split())
board = []
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)

route = [[0,1],[1,0],[-1,0],[0,-1]]

def dfs(i, j):
    dq = deque([(i, j)])
    visited_lst = [(i, j)]

    while len(dq) != 0:
        loc = dq.popleft()
        for move in route:
            new_loc = (loc[0] + move[0], loc[1] + move[1])
            if 0 <= new_loc[0] < n and 0 <= new_loc[1] < n:
                if l <= abs(board[new_loc[0]][new_loc[1]] - board[loc[0]][loc[1]]) <= r:
                    if new_loc not in visited_lst and visited[new_loc[0]][new_loc[1]] == 0:
                        dq.append(new_loc)
                        visited_lst.append(new_loc)

    if len(visited_lst) > 1:
        value = 0
        for v in visited_lst:
            value += board[v[0]][v[1]]
        value = value // len(visited_lst)

        for v in visited_lst:
            board[v[0]][v[1]] = value

    return visited_lst


cnt = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited_lst = dfs(i,j)
                if len(visited_lst) > 1:
                    for v in visited_lst:
                        visited[v[0]][v[1]] = 1
                    flag = True
                else:
                    visited[i][j] = 1
    if flag == False:
        break
    
    cnt += 1

print(cnt)