# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        if len(s) >= k:

            def recur(s):
                res = 0
                if len(s) < k:
                    return 0
                for i in range(0, len(s)):
                    
                    curr = s[:i+k]
                    n = len(curr)
                    if n < k:
                        break
                    count = {}
                    for j in curr:
                        if j not in count.keys():
                            count[j] = 1
                        else:
                            count[j] += 1

                    length = 0
                    flag = 0
                    for key,val in count.items():
                        if val >= k and flag == 0:
                            length += val
                            flag = 0
                        else:
                            flag = 1
                    if flag == 0:
                        res = max(length, res)
                
                return res
            
            i = 0
            max_ = 0
            n = len(s)

            if s.count(s[0]) == len(s):
                return len(s)

            while i < n:
                string = s[i:]
                lcount = recur(string)
                max_ = max(max_, lcount)
                i += 1
            
            return max_
        
        else:
            return 0
        '''
        
        
        
        problematic_letters = []
        valid = True
        counter = Counter(s)
        
        for letter in counter:
            if counter[letter] < k:
                problematic_letters.append(letter)
                valid = False
        if valid:
            return len(s)
        
        for letter in problematic_letters:
            s = s.replace(letter, ' ')
        strings_after_divide = s.split()

        ans = 0
        for string in strings_after_divide:
            ans = max(ans, self.longestSubstring(string, k))
        return ans