arr = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]


def sol(l, n, k):
    res = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for m in range(j + 1, n):
                res.add(l[i] + l[j] + l[m])
    res = list(res)
    res.sort(reverse=True)
    return res[k - 1]


print(sol(arr, 10, 3))
