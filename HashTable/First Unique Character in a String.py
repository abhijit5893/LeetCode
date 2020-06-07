# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = dict()
        for i in s:
            if table.get(i, None) is not None:
                table[i] += 1
            else:
                table[i] = 1

        for i in table.keys():
            if table[i] == 1:
                return s.index(i)

        return -1

        '''
        Optimal solution
        for i,j in OrderedDict(Counter(s)).items():
            if j == 1:
                return s.index(i)
        return -1
        '''