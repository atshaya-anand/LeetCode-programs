# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashTable = {}
        for i in range(len(order)):
            hashTable[order[i]] = i
        
        for i in range(1,len(words)):
                a = words[i-1]
                b = words[i]
                j = 0
                while j < len(a):
                    if j > len(b)-1:
                        return False
                    if hashTable[a[j]] < hashTable[b[j]]:
                        break
                    elif hashTable[a[j]] == hashTable[b[j]]:
                        j += 1
                        continue
                    else:
                        return False
                    j += 1
            
        return True