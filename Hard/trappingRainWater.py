# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        
        max_ = -1
        for i in range(n):
            max_ = max(max_,height[i])
            left[i] = max_
        
        max_ = -1
        for i in range(n-1,-1,-1):
            max_ = max(max_,height[i])
            right[i] = max_
        
        water = 0
        for i in range(n):
            water += min(left[i],right[i]) - height[i]
        
        return water