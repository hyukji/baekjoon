N = int(input())
MAX_FIVE = N // 5

for f in range(MAX_FIVE, -1, -1):
    if (N - 5*f) % 3 == 0:
        print(f + (N - 5*f) // 3)
        break
else:
    print(-1)