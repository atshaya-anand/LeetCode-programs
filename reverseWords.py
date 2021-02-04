# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        s = s.strip()
        str_list = s.split(" ")
        str_list.reverse()
  
        for i in range(len(str_list)):
            if str_list[i] != '':
                if i != len(str_list)-1:
                    res = res + str_list[i] + ' '
                else:
                    res += str_list[i]
            
        return res