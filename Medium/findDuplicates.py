# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        val = {}
        output = []
        if len(nums) >= 1:
            val[nums[0]] = 0
        for i in range(1,len(nums)):
            if nums[i] not in val.keys():
                val[nums[i]] = 0
            else:
                output.append(nums[i])
        return output