# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for i in nums:
            j = 0
            if i not in res:
                res.add(i)
            else:
                return True