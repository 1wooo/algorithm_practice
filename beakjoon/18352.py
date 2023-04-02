import heapq
import sys
input = sys.stdin.readline

# 18352 특정 거리의 도시 찾기

INF = int(1e9)

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    c1, c2 = map(int, input().split())
    arr[c1].append(c2)


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for j in arr[now]:
            cost = dist + 1
            if cost < distance[j]:
                distance[j] = cost
                heapq.heappush(q, (cost, j))

dijkstra(x)

cnt = 0
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        cnt += 1

if cnt == 0:
    print(-1)