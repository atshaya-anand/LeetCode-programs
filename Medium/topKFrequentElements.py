# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val = {}
        for i in nums:
            if i not in val.keys():
                val[i] = nums.count(i)
        sorted_keys = sorted(val, key=val.get, reverse=True)
        return sorted_keys[:k]