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
    heapq.heappush(q, (start, 0))

    while q:
        now, now_cost = heapq.heappop(q)

        if distance[now] < now_cost:
            continue

        for j in arr[now]:
            cost = now_cost + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (j[0], cost))

max_cost = 0
for i in range(1, n+1):
    distance = [INF] * (n + 1)
    dijkstra(i, distance)
    print(distance[x])
    max_cost = max(max_cost, distance[x])

print(max_cost)

