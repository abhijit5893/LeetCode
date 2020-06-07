# https://leetcode.com/problems/single-number/
class Solution:
    '''
    XOR operation will cancel out pairs of numbers
    '''
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            print(num, res)
            res ^= num
        return res
        '''
        a = {}
        for i in nums:
            if a.get(i, None) is None:
                    a[i] = 1
            else:
                a[i] += 1
        for i in a.keys():
            if a[i] == 1:
                return i
        return 0
        '''     
