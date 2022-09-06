N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())
 

W_chess = (("WB" * 4) + ("BW" * 4))*4
min_diff = 64
for m in range(M-7): 
    for n in range(N-7): 
        cut_board = ""
        diff = 0
        for i in range(8):
            cut_board += board[n+i][m : m+8]
        for i in range(64):
            if W_chess[i] != cut_board[i]:
                diff += 1
        diff = diff if diff <= 32 else 64-diff
        if diff < min_diff: min_diff = diff

print(min_diff)

