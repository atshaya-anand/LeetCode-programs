# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                sum = 0
                if i == j:
                    continue
                else:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        output.append(i)
                        output.append(j)
                        return output