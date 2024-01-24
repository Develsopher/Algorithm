# 대표값
# n 명의 학생 수학점수 -> 평균점수 반올림
# 평균에 가장 가까운학생 몇번째 학생
# 점수가 높은학생 -> 번호가빠른학생

import math

list = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]


def sol(l):
    avg = sum(list) / len(list)
    avg = avg + 0.5
    avg = int(avg)
    minDiff = 21470000
    for idx, x in enumerate(l):
        tmp = abs(x - avg)
        if tmp < minDiff:
            minDiff = tmp
            score = x
            res = idx + 1
        elif tmp == minDiff:
            if x > score:
                score = x
                res = idx + 1
    print(score, res)


sol(list)
