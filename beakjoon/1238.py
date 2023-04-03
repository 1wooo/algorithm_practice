import heapq
import sys
input = sys.stdin.readline

# 1238 파티
INF = int(1e9)

n,m,x = map(int,input().split())
arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b, cost = map(int,input().split())
    arr[a].append((b, cost))

def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        now_cost, now = heapq.heappop(q)

        if distance[now] < now_cost:
            continue

        for j in arr[now]:
            cost = now_cost + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

max_cost = 0
for i in range(1, n+1):
    if i == x:
        continue
    distance1 = [INF] * (n + 1)
    distance2 = [INF] * (n + 1)

    dijkstra(i, distance1)
    dijkstra(x, distance2)

    tmp_cost = distance1[x] + distance2[i]
    max_cost = max(max_cost, tmp_cost)


print(max_cost)

