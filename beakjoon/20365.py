import sys
input = sys.stdin.readline

## 백준 20365

n = int(input())
b = input()

color = {'B' : 0, 'R' : 0}
color[b[0]] += 1

for i in range(1, n):
    if b[i-1] != b[i]:
        color[b[i]] += 1
print(color)
print(min(color['B'], color['R']) + 1)

# 같은 색깔은 한번에 칠할 수 있으니까 카운트 안올리고 다른색이 나오면 해당 색깔 카운트 올리기
# 결과적으로 두 색깔중 적게 칠하는 색깔+1 이 답이다
# 이유는 간단하다. 예를들어 파란색을 칠하는 카운트 수가 적다면
# 먼저 빨간색으로 한번에 칠한 뒤에 파란색을 하나하나 칠하게 되는 경우가 최소작업 횟수이기 때문.