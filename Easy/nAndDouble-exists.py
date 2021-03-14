# https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        a = set(arr)
        count = 0
    
        for i in range(len(arr)):
            c = 2*arr[i]
        
            if c == 0:
                count +=1
        
            if c in a and c!=0:
                return True
            if count > 1:
                return True
        
        return False