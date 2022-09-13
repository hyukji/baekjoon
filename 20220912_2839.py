N = int(input())
MAX_FIVE = N // 5

# for f in range(MAX_FIVE, -1, -1):
#     if (N - 5*f) % 3 == 0:
#         print(f + (N - 5*f) // 3)
#         break
# else:
#     print(-1)


arr = [-1 for _ in range(N+1)]
arr[3] = arr[5] = 1
for i in range(6, N+1, 1):
    if arr[i-3] != -1 and arr[i-5] != -1:
        arr[i] = min(arr[i-3], arr[i-5])
    else:
        arr[i] = max(arr[i-3], arr[i-5])
    
    if arr[i] != -1:
        arr[i] += 1

print(arr[i]) 