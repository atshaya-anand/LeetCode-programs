# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        val = dict()
        val["I"] = 1
        val["V"] = 5
        val["X"] = 10
        val["L"] = 50
        val["C"] = 100
        val["D"] = 500
        val["M"] = 1000

        res = 0
  
        if "IV" in s:
            res += 4
            s = s.replace("IV",'')
        if "IX" in s:
            res += 9
            s = s.replace("IX",'')
        if "XL" in s:
            res += 40
            s = s.replace("XL",'')
        if "XC" in s:
            res += 90
            s = s.replace("XC",'')
        if "CD" in s:
            res += 400
            s = s.replace("CD",'')
        if "CM" in s:
            res += 900
            s = s.replace("CM",'')
  
        for i in s:
            if i in val.keys():
                res += val[i]
  
        return res