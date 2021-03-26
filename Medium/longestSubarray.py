# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq, maxq = deque(), deque()
        i = 0
        res = 0
        for j, n in enumerate(nums):
            while minq and minq[-1] > n: minq.pop()
            while maxq and maxq[-1] < n: maxq.pop()
            minq.append(n)
            maxq.append(n)

            while i<len(nums) and minq and maxq and maxq[0]-minq[0] > limit:
                if maxq[0] == nums[i]: maxq.popleft()
                if minq[0] == nums[i]: minq.popleft()
                res = max(res, j-i)
                i+=1
        return max(res, len(nums)-i)