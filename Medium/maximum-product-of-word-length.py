# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_ = []
        for i in range(len(words)):
            j = i + 1
            while j < len(words):
                res = [1 for ch in words[i] if ch in words[j]]
                if 1 not in res:
                    l1 = len(words[i])
                    l2 = len(words[j])
                    val = l1 * l2
                    max_.append(val)
                j += 1
        if max_:
            return max(max_)
        else:
            return 0