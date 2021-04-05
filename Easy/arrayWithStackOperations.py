# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        size = 0
        
        for i in range(1,n+1):
            if i in target:
                output.append("Push")
                size += 1
                if size == len(target):
                    break
            else:
                output.append("Push")
                output.append("Pop")
        return output