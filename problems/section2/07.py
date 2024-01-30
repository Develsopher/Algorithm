# 소수의 개수 구하기
# 에라토스테네스 체


def sol(n):
    cnt = 0
    ch = [0] * (n + 1)

    for i in range(2, n + 1):
        if ch[i] == 0:
            cnt += 1
            for j in range(i, n + 1, i):
                ch[j] = 1
    return cnt


print(sol(20))
