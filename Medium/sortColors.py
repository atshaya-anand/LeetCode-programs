# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(0,n-1):
            j = i+1
            while i < j and j < n:
                if nums[i] >= nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                j += 1