N, m = map(int, input().split())
s = list(map(int, input().split()))
dp = [0 for _ in range(N)]

# def GetScore(n, s):
#     if n == 0:
#         dp[0]= s
#     elif n < 0: 
#         return -1

#     for before_s in s:
#         if GetScore(n, before_s) == -1:
#             continue
#         dp[n] = max(dp[n], GetScore(n, before_s))
#     else:
#         if dp[n] == 0:
#             return -1
    # return 


# print(GetScore(0))

