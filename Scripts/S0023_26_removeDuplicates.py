# forward traversal
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        compare_var = 'a'
        while i < len(nums):
            if nums[i] == compare_var:
                nums.remove(nums[i])
            else:
                compare_var = nums[i]
                i += 1
        print(nums)
        return i


# backward traversal
class Solution1(object):
    def removeDuplicates(self, nums):
        for num_index in range(len(nums) - 1, 0, -1):
            if nums[num_index] == nums[num_index - 1]:
                nums.pop(num_index)
        return len(nums)


class Solution2(object):
    def removeElement(self, nums, val):
        cnt = len(nums)
        for i in range(cnt - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        print(nums)
        return len(nums)


class Solution3(object):
    def removeElement(self, nums, val):
        nums.sort(key=lambda x: x == val)
        return (len(nums) - nums.count(val))


s = Solution3()
# print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
# print(s.removeDuplicates([-1, 0, 0, 0, 0, 3, 3]))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(s.removeElement([3, 2, 2, 3], 3))
