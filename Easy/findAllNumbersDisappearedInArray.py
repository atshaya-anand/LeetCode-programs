# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 1
        n = len(nums)
        res = []
        num = set()
        for n in nums:
            if n not in num:
                num.add(n)
        
        while i <= len(nums):
            if i not in num:
                res.append(i)
            i += 1
        
        return res