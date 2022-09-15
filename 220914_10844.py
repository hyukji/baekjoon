n = int(input())

arr = [[1 for _ in range(10)]]
arr += [[0] *(10) for _ in range(n-1)] 

for i in range(1,n):
    for j in range(10):
        if j == 0:
            arr[i][j] = arr[i-1][1]
        elif j == 9:
            arr[i][j] = arr[i-1][8]
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

res = 0
for a in arr:
    res += sum(a[1:]) % 10**9

print(res % 10**9)