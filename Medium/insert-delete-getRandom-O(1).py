# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mySet = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.mySet:
            return False
        else:
            self.mySet.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.mySet:
            self.mySet.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.mySet:
            return self.mySet[random.randint(0, len(self.mySet) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()