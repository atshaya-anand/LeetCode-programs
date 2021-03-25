# https://leetcode.com/problems/count-largest-group/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n < 10:
            return n
        res = {}
        for i in range(1,n+1):
            s=sum([int(k) for k in str(i)])
            if s in res:
                res[s].append(i)
            else:
                res[s]=[i]
        print(res)   
        resCounts = [len(i) for i in res.values()]
        print(resCounts)
        return resCounts.count(max(resCounts))