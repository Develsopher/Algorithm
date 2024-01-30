# 각 자리숫의 합
list = [125, 15232, 97]


def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum
    # while x > 0:
    #     sum += x % 10
    #     x = x // 10
    # return sum


def sol(l):
    max = -214700000
    for x in l:
        tot = digit_sum(x)
        if tot > max:
            max = tot
            res = x
    return res


print(sol(list))
