# https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
            count = len(set(candyType))
            length = len(candyType)
            ans = length // 2
        
            if ans >= count:
                return count
            else:
                return ans