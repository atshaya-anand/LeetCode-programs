# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        keyboard = {'0':"qwertyuiop",
                    '1':"asdfghjkl",
                    '2':"zxcvbnm"}
        
        ans = []
        
        for word in words:
            res = []
            for char in word:
                if char in keyboard['0']:
                    res.append(0)
                    continue
                
                elif char in keyboard['1']:
                    res.append(1)
                    continue
                
                elif char in keyboard['2']:
                    res.append(2)
                    continue
            
            if res.count(res[0]) == len(res):
                ans.append(word)
            
        return ans