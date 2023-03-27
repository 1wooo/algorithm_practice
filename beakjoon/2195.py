# B2195 문자열복사 (그리디)

import copy

S = input()
P = input()

P_copy = copy.deepcopy(P)

start = 0
end = len(P)
cnt = 0
tmpStr = ""


while tmpStr != P_copy:
    flag = 0
    while flag == 0:
        tmp = P[start:end]
        if tmp in S:
            tmpStr = tmpStr + tmp
            cnt += 1
            flag = 1

            a = list(P)
            del a[start:end]
            P = "".join(a)
            end = len(P)

        else: end -= 1

print(cnt)