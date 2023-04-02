import heapq
import math
import sys
input = sys.stdin.readline

# 5972 택배 배송

INF = int(1e9)
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for j in arr[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0],))

dijkstra(1)

print(distance[n])