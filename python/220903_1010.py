def n_brige(N, M):
    dp = [[0]* M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i == 0:
                dp[i][j] = j + 1
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

    return dp[N-1][M-1]         

TC = int(input())
for i in range(TC):
    N, M = map(int, input().split())
    print(n_brige(N, M))
    
