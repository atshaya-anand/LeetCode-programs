# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        def checkTravel(petrol,index):
            n = len(gas)
            i = index
            petrol = gas[index]
            petrol -= cost[index]
            if petrol < 0: 
                return False
            index += 1
            if index == n:
                index = 0
            while index != i:
                petrol += gas[index]
                petrol -= cost[index]
                if petrol < 0:
                    return False
                index += 1
                if index == n:
                    index = 0
            return True
        
        for i in range(len(gas)):
            petrol = 0
            if gas[i] >= cost[i]:
                if checkTravel(petrol,i):
                    return i
        
        return -1