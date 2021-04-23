# https://leetcode.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.hashMap = {}

    def get(self, key: int) -> int:
        keys = list(self.hashMap.keys())
        #print(keys)
        if len(keys) == 0:
            return -1
        for i in keys:
            if i == key:
                val = self.hashMap[key]
                del self.hashMap[key]
                self.hashMap[key] = val
                return val
        return -1

    def put(self, key: int, value: int) -> None:
        keys = list(self.hashMap.keys())
        if key in keys:
            del self.hashMap[key]
            self.hashMap[key] = value
        elif len(keys) < self.size:
            self.hashMap[key] = value
        elif len(keys) >= self.size:
            del self.hashMap[keys[0]]
            self.hashMap[key] = value
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)