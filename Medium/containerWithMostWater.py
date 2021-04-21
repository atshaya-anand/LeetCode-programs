# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        first = 0
        last = n - 1
        max_ = -1
        
        while first < last:
            max_ = max(max_,min(height[first],height[last])*(last-first))
            if height[first] > height[last]:
                last -= 1
            else:
                first += 1
                
        return max_