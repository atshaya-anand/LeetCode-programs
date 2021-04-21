# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = ''
        for i in t:
            if i in s and t.count(i) == s.count(i):
                continue
            elif i in s and t.count(i) > s.count(i):
                diff = t.count(i) - s.count(i)
                for j in range(diff):
                    res += i
                t = list(t)
                t.remove(i)
                t = ''.join(t)
            else:
                res += i
        return res