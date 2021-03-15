# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        output = 0
        for arr in arr1:
            for array in arr2:
                if abs(arr-array) <= d:
                    count += 1
                    break
                else:
                    count = 0
            if count == 0:
                output += 1
        return output