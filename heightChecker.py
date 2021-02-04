# https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        
        if len(heights) <= 1:
            return 0
        
        else:
            copy_arr = [x for x in heights]
            copy_arr.sort()
    
            for i in range(len(heights)):
                if copy_arr[i] == heights[i]:
                    continue
                else:
                    count += 1

            return count