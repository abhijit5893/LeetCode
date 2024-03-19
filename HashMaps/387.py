#387. First Unique Character in a String

'''
Hash Table solution
Space - O(n)
Time -O(n)
'''
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = collections.defaultdict()
        for i in range(len(s)):
            if table.get(s[i]):
                table[s[i]].append(i)
            else:
                table[s[i]] = [i]
        for c in s:
            if len(table[c]) == 1:
                return table[c][0]
        return -1