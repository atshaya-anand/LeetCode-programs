# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        Sum = 0
        while num:
            rem = num % 10
            Sum += rem
            num = num // 10
        if Sum < 10:
            return Sum
        else:
            return self.addDigits(Sum)