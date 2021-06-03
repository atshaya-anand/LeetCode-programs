# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num = set()
        for num_ in nums:
            if num_ not in num:
                num.add(num_)
        i = 1
        while i:
            if i not in num:
                return i
            i += 1