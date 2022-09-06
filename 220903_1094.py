x = int(input())

lst = [64,32,16,8,4,2,1]
cnt = 0

while True:
    stick = lst.pop(0)
    if stick == x:
        print(cnt + 1)
        break
    elif stick < x:
        cnt += 1
        x -= stick

