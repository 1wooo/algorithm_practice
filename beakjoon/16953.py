import sys
input = sys.stdin.readline

a, b = map(int,input().split())
cnt = 1

while b != a:
    tmp = b
    if b % 10 == 1 and (b // 10) >= a:
        b //= 10
        cnt += 1

    elif b % 2 == 0:
        b //= 2
        cnt += 1

    if tmp == b:
        print(-1)
        break
else:
    print(cnt)