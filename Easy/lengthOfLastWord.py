# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = []
        res = s.split(" ")
        i = len(res) - 1
        while i >= 0:
            if len(res[i]) > 0:
                return len(res[i])
            else:
                i -= 1
        return 0