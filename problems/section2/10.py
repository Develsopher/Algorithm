# 점수계산
list = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]


def sol(l):
    res = 0
    score = 0
    for x in l:
        if x == 1:
            score += 1
            res += score
        else:
            score = 0
    return res


print(sol(list))
