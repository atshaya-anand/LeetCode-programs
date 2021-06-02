# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        ans = []
        
        for i in range(0,len(strs)):
            
            if strs[i] == "":
                str_ = ""
                str_ += strs[i]
            
            else:
                str_ = strs[i]
            
            if i != 0:
                str2 = sorted(str_)
                str2 = ''.join(str2)
                if str2 in res.keys():
                    res[str2].append(str_)
                else:
                    res[str2] = [str_]
        
            else:
                temp = sorted(str_)
                temp = ''.join(temp)
                res[temp] = [str_]
            
            
        for key,value in res.items():
            ans.append(value)
        
        return ans         