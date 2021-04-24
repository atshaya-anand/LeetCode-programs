# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        num_stack, sign_stack = [], []
        cur_sum, i, cur_sign = 0, 0, 1
        while i < len(s):
            x = s[i]
            if x.isspace():
                i += 1
                continue
            if x == '+':
                cur_sign = 1
                i += 1
            elif x == '-':
                cur_sign = -1
                i += 1
            elif x == '(':
                sign_stack += [cur_sign]
                num_stack += [cur_sum]
                cur_sum = 0
                cur_sign = 1
                i += 1
            elif x == ')':
                prev_sum = num_stack.pop()
                prev_sign = sign_stack.pop()
                cur_sum = cur_sum * prev_sign + prev_sum
                i += 1
            else:
                cur_num = 0
                while i < len(s) and s[i].isdigit():
                    cur_num = 10 * cur_num + int(s[i])
                    i += 1
                cur_num *= cur_sign
                cur_sum += cur_num
        return cur_sum