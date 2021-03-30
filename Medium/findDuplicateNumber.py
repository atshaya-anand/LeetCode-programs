# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums.count(nums[i]) >= 2:
                return nums[i]