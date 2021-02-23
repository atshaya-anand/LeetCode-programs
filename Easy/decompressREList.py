# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        if len(nums) % 2 == 0:
            for i in range(len(nums)):
                if i % 2 == 0:
                    freq = nums[i]
                    while freq >= 1:
                        output.append(nums[i+1])
                        freq = freq - 1
        return output