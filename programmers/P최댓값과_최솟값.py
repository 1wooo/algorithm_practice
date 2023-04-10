from collections import deque

# 프로그래머스 올바른 괄호
def solution(s):
    li = deque(list(s))
    stack = []

    if li[0] == ')':
        return False

    for i in range(len(li)):
        if len(li) == 0:
            break

        if len(stack) == 0:
            stack.append(li.popleft())

        if len(li) == 0:
            break

        if stack[-1] == li[0]:
            stack.append(li.popleft())
        elif stack[-1] == '(' and li[0] == ')':
            stack.pop()
            li.popleft()
    return len(stack) == 0