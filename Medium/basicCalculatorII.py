# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        def precedence(op):
            if op == '+' or op == '-':
                return 1
            if op == '*' or op == '/':
                return 2
            return 0
        def applyArithmetic(a,b,op):
            if op == "+":   return a+b
            if op == "-":   return b-a
            if op == "*":   return a*b
            if op == "/":   return b//a
        
        values = []
        operators = []
        
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i].isdigit():
                val = 0
                while i < len(s) and s[i].isdigit():
                    val = (val * 10) + int(s[i])
                    i += 1
                values.append(val)
                i -= 1
            else:
                while operators and precedence(operators[-1]) >= precedence(s[i]):
                    val1 = values.pop()
                    val2 = values.pop()
                    op = operators.pop()
                    values.append(applyArithmetic(val1,val2,op))
                operators.append(s[i])
            i += 1
        
        while operators:
            val1 = values.pop()
            val2 = values.pop()
            op = operators.pop()
            values.append(applyArithmetic(val1,val2,op))
        
        return values[-1]