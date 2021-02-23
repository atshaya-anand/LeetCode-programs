# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            st = ''
            var = strs[0]
            for s in range(1,len(strs)):
                word = strs[s]
                i = len(var)
                while i >= 0:
                    if var[:i] in word[:i]:
                        var = var[:i]
                        st = var
                        break
                    i -= 1
      

            if st != '':
                return st
            else:
                return ''