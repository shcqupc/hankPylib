def maxFact(nums):
    unchecked = 0
    checked = 0
    for i in range(len(nums)):
        unchecked_temp = max(unchecked, checked)  # 当前状态不选的情况，可能前一个选，也可能不选
        checked = unchecked + nums[i]  # 当前状态选的情况，必须是前一个不选
        unchecked = unchecked_temp
    return max(unchecked, checked)


print(maxFact([1, 2, 100, 1]))
