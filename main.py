import heapq
import sys
input = sys.stdin.readline

# 1238 파티
INF = int(1e9)

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, cost = map(int,input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for j in graph[now]:
            cost = dist + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

    return distance

max_cost = 0
for i in range(1, n+1):
    if i == x:
        continue

    # i에서 x까지의 최단 거리
    arr1 = dijkstra(i)

    # x에서 i까지의 최단 거리
    arr2 = dijkstra(x)

    # i번째 학생이 파티에 참석하고 오가는 데 걸리는 시간
    tmp_cost = arr1[x] + arr2[i]
    max_cost = max(max_cost, tmp_cost)

print(max_cost)
