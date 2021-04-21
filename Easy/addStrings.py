# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        val = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        
        def strToInt(num):
            n = 0
            for i in num:
                n = n * 10 + val[i]
            return n
        
        return str(strToInt(num1) + strToInt(num2))