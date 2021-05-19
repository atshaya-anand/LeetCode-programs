# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            count = 0
            if i == 0:
                j = 1
                while j < len(nums):
                    if nums[j] < nums[i]:
                        count += 1
                    j += 1
            elif i == len(nums)-1:
                j = 0
                while j < i:
                    if nums[j] < nums[i]:
                        count += 1
                    j += 1
            else:
                j = 0
                while j != i:
                    if nums[j] < nums[i]:
                        count += 1
                    j += 1
                j = i + 1
                while j < len(nums):
                    if nums[j] < nums[i]:
                        count += 1
                    j += 1
            output.append(count)
        return output