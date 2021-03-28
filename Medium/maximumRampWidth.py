# https://leetcode.com/problems/maximum-width-ramp/

class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        '''
        rampWidth = []
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if i < j and A[i] <= A[j]:
                    rampWidth.append(j-i)
                else:
                    continue
        if len(rampWidth) >= 1:
            return max(rampWidth)
        else:
            return 0
        '''
        stack = []
        res = 0
        for i in range(len(A))[::-1]:
            if not stack or A[i] > stack[-1][0]:
                stack.append([A[i], i])
            else:
                j = stack[bisect.bisect(stack, [A[i], i])][1]
                res = max(res, j - i)
        return res