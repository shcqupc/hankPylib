class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)): 
            for j in range(len(nums)-i-1): 
                if nums[i]+nums[i+j+1] == target:
                    return [i,i+j+1]
                

s = Solution1()
rslt = s.twoSum([2, 7, 11, 15],13)
print(rslt)

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
        head = 0
        tail = len(nums) - 1
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        while sum_result != target:
            if sum_result > target:
                tail -= 1
            elif sum_result < target:
                head += 1
            sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        return [sorted_id[head], sorted_id[tail]]

s = Solution2()
rslt = s.twoSum([2, 7, 11, 15],13)
print(rslt)

class Solution3(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for idx, value in enumerate(nums):
            chk = target - value
            if chk in list(hashmap.values()):
                return [list(hashmap.keys())[list(hashmap.values()).index(chk)], idx]
            else:
                hashmap.setdefault(idx, value)
                
            #if chk in hashmap:
                #return [hashmap[chk], idx]
            #hashmap[value]=idx

            print('hashmap:',hashmap)
        return None

s = Solution3()
rslt = s.twoSum([2, 11, 7, 15],17)
print(rslt)

