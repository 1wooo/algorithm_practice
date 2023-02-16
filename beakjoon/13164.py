import sys
input = sys.stdin.readline

#13164

n,k = map(int,input().split())
height = list(map(int,input().split()))
ary = []
for i in range(1,n):
    ary.append(height[i] - height[i-1])

ary.sort()
print(sum(ary[:n-k]))
