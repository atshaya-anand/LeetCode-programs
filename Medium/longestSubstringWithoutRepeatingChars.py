# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        size = len(s)
        if size <= 0:
            return 0
        elif s[0] * size == s:
            return 1
        res = []
        i = 0
        strr = ''
        
        while i < size-1:
            j = i+1
            if s[i] not in strr:
                strr += s[i]
            if s[i] != s[j] and s[j] not in strr:
                strr += s[j]
                if strr not in res:
                    res.append(strr)
                print(strr)
            else:
                strr = ''
            i += 1
        res = [len(i) for i in res]
        return max(res)
        '''
        
        longest = 0
        left, right = 0, 0
        chars = set()
        while left < len(s) and right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(s[left])
                left += 1
        return longest