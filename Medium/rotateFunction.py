# https://leetcode.com/problems/rotate-function/

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        arr_sum = sum(nums)
        sum_of_products = 0
        for i,val in enumerate(nums):
            sum_of_products+= i*val
            
        n = len(nums)
        max_val = sum_of_products
        for i in range(1,n):
			# A[-i] is the last val after each shift.
            sum_of_products+=(arr_sum-(nums[-i]*n))
            max_val = max(max_val ,sum_of_products)
        return max_val