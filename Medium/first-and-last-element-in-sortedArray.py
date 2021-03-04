# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return [-1,-1]
        else:
            output = []
            flag = 0
            index = 0
            for i in range(len(nums)):
                if nums[i] == target:
                    output.append(i)
                    flag += 1
                    index = i
            if flag == 0:
                return [-1,-1]
            elif flag == 1:
                return [index,index]
            else:
                if len(output) > 2:
                    return [output[0],output[len(output)-1]]
                else:
                    return output