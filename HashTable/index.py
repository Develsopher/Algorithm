# input: nums = [4,1,9,7,5,3,16] target: 14
# outPut: true


def two_sum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = 1

    for v in nums:
        needed_number = target - v
        if needed_number in memo and v != needed_number:
            return True
    return False


# print(two_sum([4, 1, 9, 7, 5, 3, 16], 14))

print(two_sum([4, 1, 9, 7, 8, 2], 14))
