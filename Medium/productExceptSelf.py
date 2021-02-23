# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_array=[]
        right_array=[]
        
        left_array.append(1)
        right_array.append(1)
        
        for i in range(1,len(nums)):
            
            left_array.append(left_array[i-1]*nums[i-1])
            right_array.append(right_array[i-1]*nums[len(nums)-i])
        
        
        right_array=right_array[::-1]
        
        return_array=[]
        
        for i in range(len(nums)):
            return_array.append(left_array[i]*right_array[i])
            
        
        return return_array