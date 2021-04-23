# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            max_ = max(nums)
            nums.remove(max_)
        return max_