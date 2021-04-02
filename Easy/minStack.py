# https://leetcode.com/problems/min-stack/

import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.stack)

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minimum = min(self.stack)

    def top(self) -> int:
        n = len(self.stack)
        return self.stack[n-1]

    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()