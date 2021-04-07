# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            leftSum = 0
            rightSum = 0
            if i == 0:
                leftSum = 0
                rightSum = sum(nums[i+1:len(nums)])
                if leftSum == rightSum:
                    return i
            elif i == len(nums)-1:
                rightSum = 0
                leftSum = sum(nums[:len(nums)-1])
                if leftSum == rightSum:
                    return i
            else:
                leftSum = sum(nums[0:i])
                rightSum = sum(nums[i+1:len(nums)])
                if leftSum == rightSum:
                    return i
        
        return -1