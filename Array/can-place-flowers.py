#https://leetcode.com/problems/can-place-flowers/
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count  = 0
        s = len(flowerbed)
        if n == 0: return True
        if s == 1: return count == flowerbed[0]
        for i in range(s):

            if flowerbed[i] == 0:
                #left
                if  i== 0 and flowerbed[i+1] <= 0:
                    flowerbed[i+1] = -1
                    count += 1
                elif  i == s-1 and flowerbed[i-1] <= 0:
                    flowerbed[i-1] = -1
                    count += 1
                else:
                    if flowerbed[i-1] <= 0 and flowerbed[i+1] <= 0:
                        flowerbed[i-1] = flowerbed[i+1] = -1
                        count += 1

        return count >= n

        '''
        pad_flowerbed = [0] + flowerbed + [0]
        count = 0
        for idx in range(len(flowerbed)):
            if pad_flowerbed[idx:idx+3] == [0, 0, 0]:
                pad_flowerbed[idx+1]=1
                count+=1
        return count >= n
        '''