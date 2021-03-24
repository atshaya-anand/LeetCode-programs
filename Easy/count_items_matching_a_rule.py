# https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        val = {'type':0,'color':1,'name':2}
        for item in items:
            if item[val[ruleKey]] == ruleValue:
                count += 1
        return count