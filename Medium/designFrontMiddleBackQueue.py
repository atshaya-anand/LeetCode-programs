# https://leetcode.com/problems/design-front-middle-back-queue/

class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        mid = (len(self.queue)) // 2
        self.queue.insert(mid, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if self.queue:
            return self.queue.pop(0)
        return -1

    def popMiddle(self) -> int:
        if self.queue:
            mid = (len(self.queue) - 1) // 2
            return self.queue.pop(mid)
        return -1

    def popBack(self) -> int:
        if self.queue:
            return self.queue.pop()
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()