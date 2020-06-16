# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits) - 1 - i))
        return [int(i) for i in str(num + 1)]

        '''
        number = 0
        s = len(digits) -1
        for i in digits:
            number += i * (10**(s))
            s-= 1
        print(number, number+1)
        number = number +1
        out = []
        while number >= 1:
            out.append(number%10)
            number  //=10
        return out[::-1]
        '''