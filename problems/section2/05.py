# 정다면체
def sol(n, m):
    cnt = [0] * (n + m + 3)
    max = -217400000
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cnt[i + j] += 1

    for i in range(n + m + 1):
        if cnt[i] > max:
            max = cnt[i]

    for i in range(n + m + 1):
        if cnt[i] == max:
            print(i, end=" ")


print(sol(4, 6))
