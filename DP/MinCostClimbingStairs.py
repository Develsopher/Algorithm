cost = [10, 15, 20, 17, 1]
memo = {}


# top - down
# O(2n) -> O(n)
def dp(n):
    if n == 0 and n == 1:
        return 0
    if n not in memo:
        memo[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])
    return memo[n]


# bottom - up
def dp2(n):
    # 배열
    memo = [-1] * n
    memo[0] = 0
    memo[1] = 0
    for i in range(2, n + 1):
        memo[i] = min(memo[i - 1] + cost[i - 1], memo(i - 2) + cost[i - 2])
    return memo[n]
