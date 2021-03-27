# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        output = [None] * (n+1)
        i = 0
        while i<len(output):
            if None not in output:
                break
            else:
                if i == 0:
                    output[i] = 0
                if i == 1:
                    output[i] = 1
                if 2*i <= n and 2 <= 2*i:
                    output[2*i] = output[i]
                if 2 <= 2*i+1 and 2*i+1 <= n:
                    output[2*i+1] = output[i] + output[i+1]
            i += 1
        return max(output)