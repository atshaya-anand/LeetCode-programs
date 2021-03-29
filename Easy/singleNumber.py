# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = {}
        for i in nums:
            if i not in val:
                val[i] = nums.count(i)
            else:
                continue
        for i,j in val.items():
            if j == 1:
                return i