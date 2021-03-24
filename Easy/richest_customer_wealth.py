# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for account in accounts:
            totalWealth = 0
            for i in account:
                totalWealth += i
            wealth.append(totalWealth)
        return max(wealth)