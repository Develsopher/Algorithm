# top-down
memo = {}


def cs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo:
        memo[n] = cs(n - 1) + cs(n - 2)

    return memo[n]


# bottom-up
memo2 = {1: 1, 2: 2}


def cs2(n):
    for i in range(3, n + 1):
        memo2[i] = memo2[i - 1] + memo2[i - 2]
    return memo2[i]
