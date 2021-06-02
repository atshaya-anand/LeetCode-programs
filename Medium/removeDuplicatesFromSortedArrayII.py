# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 1
        count = {}
        
        while start < len(nums):
            if nums[start] not in count.keys():
                count[nums[start]] = 1
            if nums[start] == nums[start-1]:
                count[nums[start]] += 1
                if count[nums[start]] > 2:
                    nums.remove(nums[start])
                    start = start
                    continue
            start += 1
                    
        return len(nums)