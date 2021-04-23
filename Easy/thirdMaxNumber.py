# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return max(nums)
        
        flag = 0
        numsCopy = nums[:]
        for i in range(3):
            if len(nums) > 0: 
                max_ = max(nums)
                nums = list(filter(lambda a: a != max_, nums))
                flag = 0
            else:
                flag = 1
        
        if flag:
            return max(numsCopy)
        else:
            return max_