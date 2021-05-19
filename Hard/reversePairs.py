# https://leetcode.com/problems/reverse-pairs/

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        count = 0
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] > 2 * nums[j]:
                    count += 1
                j += 1
        return count
        '''
        
        arr = []
        res = 0
        for num in nums:
            index = bisect.bisect_right(arr, num * 2)
            res += len(arr) - index
            bisect.insort(arr, num)
        return res