# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelsList = []
        for i in s:
            if i in 'aeiou' or i in 'AEIOU':
                vowelsList.append(i)
        vowelsList.reverse()
        s = list(s)
        count = 0
        for i in range(len(s)):
            if s[i] in 'aeiou' or s[i] in 'AEIOU':
                s[i] = vowelsList[count]
                count += 1
        res = ''
        res = res.join(s)
        return res