# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            j = i+1
            while i < j and j < n:
                if nums[i] == 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                j += 1