# https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1] and arr[i] != arr[i-1]:
                continue
            elif arr[i] == arr[i-1]:
                return False
            else:
                if i - 1 != 0: 
                    temp = arr[i:]
                    for j in range(1,len(temp)):
                        if temp[j] < temp[j-1]:
                            continue
                        elif temp[j] == temp[j-1]:
                            return False
                        else:
                            return False
                    return True
                else:
                    return False
        
        return False