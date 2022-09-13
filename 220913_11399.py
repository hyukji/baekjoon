N = int(input())
time = list(map(int, input().split()))
time.sort(reverse=True)

total_time = 0
for i in range(N):
    total_time += time[i] * (i+1)

print(total_time)
