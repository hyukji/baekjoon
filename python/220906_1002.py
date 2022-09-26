import math

TC = int(input())

for _ in range(TC):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue

    if r1 + r2 < dist:
        print(0)
    elif r1 + r2 == dist:
        print(1)
    else:
        if abs(r2 - r1) > dist:
            print(0)
        elif abs(r2 - r1) == dist:
            print(1)
        else:
            print(2)
    