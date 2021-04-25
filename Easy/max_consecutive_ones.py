# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max_ = 0
        curr = 0
        for i in range(n):
            if nums[i] == 1:
                curr += 1
                max_ = max(max_,curr)
            else:
                curr = 0
        return max_