nums = [1, 2, 3, 4]


def subset(nums, k):
    result = []

    def backtracking(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return

        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtracking(i + 1, curr)
            curr.pop()

    for k in range(len(nums) + 1):
        backtracking(start=0, curr=[])

    return result


print(subset(nums, 4))
