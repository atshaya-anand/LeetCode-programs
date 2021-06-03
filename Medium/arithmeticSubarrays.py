# https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        
        for i in range(0,len(l)):
            a = l[i]
            b = r[i]
            arr = nums[a:b+1]
            arr.sort()
            flag = 0

            for j in range(1,len(arr)):
                if j+1 < len(arr):
                    if abs(arr[j] - arr[j-1]) == abs(arr[j] - arr[j+1]):
                        continue
                    else:
                        flag = 1
            if flag == 0:
                res.append(True)
            else:
                res.append(False)

        return res