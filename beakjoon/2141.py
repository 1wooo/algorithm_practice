import sys
input = sys.stdin.readline

#2141

n = int(input())
town = []
allpeople = 0

for i in range(n):
    a,b = map(int,input().split())
    town.append((a,b))
    allpeople += b

town.sort(key= lambda x:x[0])
tmp = 0
for i in range(n):
    tmp += town[i][1]

    if tmp >= allpeople / 2:
        print(town[i][0])
        break

