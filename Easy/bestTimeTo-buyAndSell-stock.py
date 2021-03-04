# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_till_now = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_till_now:
                min_till_now = price
            else:
                diff = price - min_till_now
                if max_profit < diff:
                    max_profit = diff
        return max_profit