# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def applyArithmetic(a, b, op):
            if op == '+':
                return a+b
            if op == '-':
                return b-a
            if op == '*':
                return a*b
            if op == '/':
                res = int(b/a)
                return res
        
        values = []
        
        for i in tokens:
            j = 0
            while j < len(i):
                
                if i[j].isdigit():
                    val = 0
                    while j < len(i) and i[j].isdigit():
                        val = (val * 10) + int(i[j])
                        j += 1
                    values.append(val)
                    j -= 1
                
                elif i[j] == '-' and len(i) > 1:
                    val = 0
                    while j+1 < len(i) and i[j+1].isdigit():
                        val = (val * 10) + int(i[j+1])
                        j += 1
                    
                    val = val * -1
                    values.append(val)
                
                else:
                    val1 = values.pop()
                    val2 = values.pop()
                    op = i
                    values.append(applyArithmetic(val1,val2,op))
                
                j += 1
        
        return values[-1]