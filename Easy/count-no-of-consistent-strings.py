# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            flag = 0
            for letter in word:
                if letter in allowed:
                    flag += 1
            if flag == len(word):
                count += 1
        return count