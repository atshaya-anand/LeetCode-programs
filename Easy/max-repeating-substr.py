# https://leetcode.com/problems/maximum-repeating-substring/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count=0
        word1=word
        while word1 in sequence:
            word1+=word
            count+=1
        return count