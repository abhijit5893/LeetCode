# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bit = [0] * 32
        # Counter the number of 1 for the jth position and store it in bit arrat
        for num in nums:
            for j in range(32):
                bit[j] += num >> j & 1
        res = 0
        for i, val in enumerate(bit):
            if val > len(nums) // 2:
                # if the 31th bit if 1,
                # it means it's a negative number
                if i == 31:
                    res -= (1 << 31)
                else:
                    res |= 1 << i
        return res

        ''''
        With HashTables - O(n)
        table = {}
        for i in nums:
            if table.get(i,0):
                table[i] += 1
                if table[i] > len(nums)//2:
                    return i
            else:
                table[i] = 1
                if table[i] > len(nums)//2:
                    return i
        return 0
        '''

        '''
        This is Cheating -One line answer O(nlogn) - 
        return sorted(nums)[len(nums)//2]
        '''