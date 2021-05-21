# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ind = 0
        len_ = len(nums)
        res = []
        
        if len_ < 3:
            return res
        
        sorted_nums = sorted(nums)
        while ind < len_:
            
            left = ind + 1
            right = len_ - 1

            while left < right:
                arr = [sorted_nums[ind],sorted_nums[left],sorted_nums[right]]
                sum_ = sum(arr)

                if sum_ == 0:
                    if arr not in res:
                        res.append(arr)
                    else:
                        break
                
                if sum_ < 0:
                    left += 1
                    while left < right and sorted_nums[left] == arr[1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and sorted_nums[right] == arr[2]:
                        right -= 1
                    
            ind += 1
        
        return res