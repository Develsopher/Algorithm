nums = [4, 9, 7, 5, 1]


def twosum(nums, target):
    def backtracking(start, curr):
        if len(curr) == 2 and sum(nums[i] for i in curr) == target:
            return curr

        for i in range(start, len(nums)):
            curr.append(i)
            ret = backtracking(i + 1, curr)
            if ret:
                return ret
            curr.pop()
        return None

    return backtracking(0, [])


print(twosum(nums, 12))
