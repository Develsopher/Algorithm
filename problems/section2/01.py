# K번째 약수


def sol(n, k):
    cnt = 0

    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
        if cnt == k:
            return cnt

    return -1


print(sol(6, 3))
