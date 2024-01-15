list = [5, 2, 7, 3, 8, 9]


def sol(n, s, e, k):
    arr = n[s - 1 : e]
    arr.sort()
    return arr[k - 1]


print(sol(list, 2, 5, 3))
