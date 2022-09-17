# bfs

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
start = [(r1, c1)]
finish = (r2, c2)
cnt = 0

move_lst = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
history = set(start)

def bfs(now_lst, cnt):
    route = []
    cnt += 1
    for now in now_lst:
        for move in move_lst:
            next = (now[0] + move[0], now[1] + move[1])
            if -1 < next[0] < n and -1 < next[1] < n and next not in history:
                if next == finish:
                    print(cnt)
                    return 1, 0
                
                route.append(next)

    route = set(route)
    return route, cnt

while True:
    start, cnt = bfs(start, cnt)
    if start == 1:
        break
    if not start:
        print(-1)
        break
    history.update(start)
        

