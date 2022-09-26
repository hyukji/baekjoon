#a 메모리초과... 너무 많이 저장하나?


n = int(input())
FULL = (1 << 10) -1

arr = [[0]*(FULL+1) for _ in range(10)]
for i in range(10):
    arr[i][1 << i] = 1

for i in range(1,n):
    next_arr = [[0]*(FULL+1) for _ in range(10)]
    for j in range(10):
        for k in range(FULL+1):
            if j > 0:  
                next_arr[j][k | 1 << j] = next_arr[j][k | 1 << j] + arr[j-1][k]
            if j < 9:
                next_arr[j][k | 1 << j] = next_arr[j][k | 1 << j] + arr[j+1][k]
                
    arr = next_arr

s =0
for j in range(1,10):
    s += arr[j][FULL]

print(s % 1000000000)