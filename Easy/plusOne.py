# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tempInteger = int("".join(map(str, digits)))
        tempInteger += 1
        
        tempInteger = list(map(int, str(tempInteger)))
        return tempInteger