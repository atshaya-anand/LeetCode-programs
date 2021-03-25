# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = {}
        for num in nums:
            count = 1
            if num not in val:
                val[num] = count
            else:
                val[num] = val[num] + 1
        max = -99999
        for i in val:
            if val[i] > max:
                max = val[i]
                output = i
        return output