import heapq
import sys
input = sys.stdin.readline

# 4485 녹색 옷 입은 애가 젤다지?
# 2차원 다익스트라

di = [-1,1,0,0]
dj = [0,0,-1,1]
INF = int(1e9)

def dijkstra(starti, startj, start_rupee, distance):
    q = []
    distance[starti][startj] = start_rupee
    heapq.heappush(q, (start_rupee, starti, startj))

    while q:
        dist, cur_i, cur_j = heapq.heappop(q)

        if distance[cur_i][cur_j] < dist:
            continue

        for k in range(4):
            ni = cur_i + di[k]
            nj = cur_j + dj[k]

            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue
            cost = dist + arr[ni][nj]
            if distance[ni][nj] > cost:
                distance[ni][nj] = cost
                heapq.heappush(q, (cost, ni, nj))
    return distance[n-1][n-1]

cnt = 0
while True:
    n = int(input())
    cnt += 1
    if n == 0:
        break

    distance = [[INF]*n for _ in range(n)]

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    res = dijkstra(0, 0, arr[0][0], distance)
    print(f"Problem {cnt}: {res}")




