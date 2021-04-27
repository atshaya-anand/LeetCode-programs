# https://leetcode.com/problems/longest-uncommon-subsequence-i/

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a != b:
            return max(len(a),len(b))
        return -1