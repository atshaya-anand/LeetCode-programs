# https://leetcode.com/problems/decoded-string-at-index/

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        '''
        def hasNumbers(inputString):
            return any(char.isdigit() for char in inputString)
        
        def decodeString(char):
            ind = S.index(char)
            temp = S[:ind]
            string = ''
            for k in temp:
                string += k
            num = int(i) - 1
            S[ind] = string * num
            string2 = ''
            for k in S:
                string2 += k
            S_copy = list(string2)
            return S_copy
        
        S = list(S)
        S_copy = S[:]
        
        for i in S:
            
            flag = 0
            if i.isnumeric():
                S_copy = decodeString(i)
                flag += 1
            
            if S_copy and len(S_copy) >= K:
                if hasNumbers(S[:K-1]):
                    if i.isnumeric() and flag == 0:
                        S_copy = decodeString(i)
                    else:
                        continue
                else:
                    return S_copy[K-1]
        '''
        
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N: break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N /= int(c)
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1