# https://leetcode.com/problems/shortest-completing-word/

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        strr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        licenseStr = ''
        for char in licensePlate:
            if char in strr:
                licenseStr = licenseStr + char
        licenseStr = licenseStr.lower()
        answer,shortestLength='',float('inf')
        for word in words:
            if all(licenseStr.count(c)<=word.count(c) for c in set(licenseStr)):
                if len(word)<shortestLength:
                    shortestLength=len(word)
                    answer=word
        return answer