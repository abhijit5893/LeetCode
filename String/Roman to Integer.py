#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_table = {
            'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        num = i = 0
        while i < len(s):
            if i+1 < len(s) and symbol_table.get(s[i+1], None):
                if symbol_table.get(s[i+1]) >  symbol_table.get(s[i]):
                    num += symbol_table.get(s[i+1]) - symbol_table.get(s[i])
                    i+= 2
                else:
                    num += symbol_table[s[i]]
                    i+= 1
            else:
                num += symbol_table[s[i]]
                i+= 1
        return num