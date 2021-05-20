# https://leetcode.com/problems/flatten-nested-list-iterator/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = nestedList
        self.stack = []
        self.assignStack(self.list)
    
    def assignStack(self,arr):
        for i in arr:
            if i.isInteger():
                val = i.getInteger()
                self.stack.append(val)
            else:
                val = i.getList()
                self.assignStack(val)
    
    def next(self) -> int:
        if self.stack:
            val = self.stack.pop(0)
            return val
    
    def hasNext(self) -> bool:
        if self.stack:
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())