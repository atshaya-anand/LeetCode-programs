# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max = -9999999999
        index = 0
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
                index = i
        return index