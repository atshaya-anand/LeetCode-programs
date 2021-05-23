# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        f_ind = 0
        len_ = len(nums)
        res = []
        
        if len_ < 4:
            return res
        
        sorted_nums = sorted(nums)
        while f_ind < len_:
            ind = f_ind + 1
            while ind < len_:

                left = ind + 1
                right = len_ - 1

                while left < right:
                    arr = [sorted_nums[f_ind],sorted_nums[ind],sorted_nums[left],sorted_nums[right]]
                    sum_ = sum(arr)
                    #print('-----',arr,sorted_nums)
                    if sum_ == target:
                        #print('yes')
                        if arr not in res:
                            res.append(arr)
                        else:
                            break

                    if sum_ < target:
                        #print('yesLess')
                        left += 1
                        while left < right and sorted_nums[left] == arr[2]:
                            left += 1
                    else:
                        #print('noGreat')
                        right -= 1
                        while left < right and sorted_nums[right] == arr[3]:
                            right -= 1

                ind += 1
            f_ind += 1
        
        return res