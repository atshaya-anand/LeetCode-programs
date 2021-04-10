# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        size = len(self.queue1)
        for i in range(size):
            q = self.queue1.pop(0)
            self.queue2.append(q)
        self.queue1 , self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        #print(self.queue1,self.queue2)
        if self.queue1:
            q = self.queue1.pop()
            return q

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.queue1:
            return self.queue1[-1]
        elif self.queue2:
            return self.queue2[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        #print(self.queue1,self.queue2)
        if self.queue1:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()