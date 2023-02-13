import math
import sys
input = sys.stdin.readline

## 백준 1758

n = int(input())
tips = []
for i in range(n):
    tips.append(int(input()))

tips.sort(reverse=True)
ans = 0

for i in range(n):
    tmp = tips[i]-i
    if tmp < 0:
        continue
    ans += tmp
print(ans)



