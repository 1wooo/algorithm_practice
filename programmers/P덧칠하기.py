def solution(n, m, section):
    answer = 0

    tmp = 0

    for i in section:
        if (tmp >= i):
            continue
        else:
            tmp = i+(m-1)
            answer += 1

    return answer