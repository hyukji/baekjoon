TC = int(input())
N, M = map(int, input().split())
Class = []
for i in range(N):
    row = input()
    Class += [row]

MAX_NUM = 0
bef_broken = []
for n in range(N):
    bef_desk = 1
    broken = []
    for m in range(M):
        desk = 1 if Class[n][m] == "." else 0
        if i % 2 == 1: #홀수
            if desk == 0:
                if bef_desk == 0:
                    borken_pair = (m-2, m)
                    broken += borken_pair
                    if borken_pair in bef_broken or n == 0: 
                        MAX_NUM += 1
                bef_desk = desk
            else:
                MAX_NUM += 1
        else: 
            pass

        bef_desk = desk
    bef_broken = broken

    pass


TC = int(input())
N, M = map(int, input().split())
Trans_Class = [[] for _ in range(M)]
for i in range(N):
    row = input()
    for j, r in enumerate(row):
        Trans_Class[j].append(r)
Trans_Class += ["x" for _ in range(N)]
Trans_Class += ["x" for _ in range(N)]

print(Trans_Class)

MAX_NUM = 0
for m in range(M):
    col = Trans_Class[m]
    if m % 2 == 0: #짝수 
        MAX_NUM += col.count(".")
        cnt = 1
        for i, desk in enumerate(col):
            if desk == "x":
                if Trans_Class[m+2][i] == "x":
                    cnt += 1
                    if cnt == 3 and Trans_Class[m+1][i-1] == ".":
                        MAX_NUM += 1
            else:
                cnt = 0

print(MAX_NUM)




            
                
