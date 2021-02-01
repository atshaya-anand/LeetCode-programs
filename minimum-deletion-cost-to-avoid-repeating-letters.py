# https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
            res = 0
            minn = 0
            cost_copy = []
            for i in range(len(s)):
                if i != len(s)-1:
                    j = i+1
                    if j<=len(s):
                        if j == len(s):
                            if s[i] == s[j-1]:
                                cost_copy.append(cost[i])
                                cost_copy.append(cost[j-1])
                                minn = min(cost_copy)
                                cost_copy.remove(minn)
                                res += minn
                        else:
                            if s[i] == s[j]:
                                if cost[i] not in cost_copy and cost[i] != minn:    cost_copy.append(cost[i])
                                if cost[j] not in cost_copy or cost[j] != minn:     cost_copy.append(cost[j])
                                minn = min(cost_copy)
                                cost_copy.remove(minn)
                                res += minn
                            else:
                                minn = 0
                                cost_copy = []
            return res
