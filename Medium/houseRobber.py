# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[n-1]
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=nums[1]
        for i in range(2,n):
            best=nums[i]
            for j in range(i-1):
                best=max(best,nums[i]+dp[j])
            dp[i]=best
        return max(dp)