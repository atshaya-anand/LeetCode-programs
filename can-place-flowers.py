# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if n < 1:
            return True

        for i in range(len(flowerbed)):
                
                if flowerbed[i] == 0 and len(flowerbed) == 1:
                    count = count+1
                    if count == n:
                        break
                    
                elif flowerbed[i] == 0:
                  if i == 0:        
                    if flowerbed[i+1] !=1:
                        flowerbed[i] = 1
                        count = count+1
                        if count == n:
                            break
                        
                  elif i == len(flowerbed)-1:
                      if flowerbed[i-1] != 1:
                        flowerbed[i] = 1
                        count = count+1
                        if count == n:
                            break
                        
                  else:
                      if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                        flowerbed[i] = 1
                        count = count+1
                        if count == n:
                            break
                                 
        
        if count == n:
          return True
        else:
          return False