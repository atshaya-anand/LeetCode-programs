# https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        res = ''
        for i in range(k):
            res += words[i]
            if i != k - 1:
                res += ' '
        return res