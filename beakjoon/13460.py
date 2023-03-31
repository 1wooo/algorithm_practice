import sys
from collections import deque
input = sys.stdin.readline

# 13460 구슬탈출 2
# "기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다."



def move(redi, redj, mi, mj):
    moving = 0
    ni, nj = redi, redj

    while True:
        if arr[ni+mi][nj+mj] != '#' and arr[ni+mi][nj+mj] != 'O':
            ni += mi
            nj += mj
            moving += 1
        else:
            break
    return ni,nj,moving


def bfs():
    global cnt, flag

    q = deque()
    first_red = ()
    first_blue = ()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'B':
                first_blue = (i, j)
            elif arr[i][j] == 'R':
                first_red = (i, j)

    q.append((first_red, first_blue, cnt))

    while q:
        cur_red, cur_blue, cnt = q.popleft()

        red_i = cur_red[0]
        red_j = cur_red[1]

        blue_i = cur_blue[0]
        blue_j = cur_blue[1]

        if cnt > 10:
            continue

        for k in range(4):
            nri, nrj, nrm = move(red_i, red_j,di[k], dj[k])
            nbi, nbj, nbm = move(blue_i, blue_j, di[k], dj[k])

            if arr[nbi+di[k]][nbj+dj[k]] == 'O':
                continue
            if arr[nri+di[k]][nrj+dj[k]] == 'O' and cnt < 10:
                return cnt+1

            if nri == nbi and nrj == nbj:
                if nrm > nbm:
                    nri -= di[k]
                    nrj -= dj[k]
                else:
                    nbi -= di[k]
                    nbj -= dj[k]

            if red_i == nri and red_j == nrj and blue_i == nbi and blue_j == nbj:
                continue
            q.append(((nri, nrj),(nbi,nbj),cnt+1))
    return -1





n,m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
di = [-1, 1, 0, 0] # 상하좌우
dj = [0, 0, -1, 1]
cnt = 0

print(bfs())
