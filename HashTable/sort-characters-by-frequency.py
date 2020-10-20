#https://leetcode.com/problems/sort-characters-by-frequency/
class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        d = defaultdict(lambda: [0]*52)
        for i in s:
            if d.get(ord(str(i)),None) is not None:
                d[ord(str(i))] += 1
            else:
                d[ord(str(i))] = 1

        #Sorting the dictionary by values
        return ''.join([ chr(i)*d[i] for i in  sorted(d, key= lambda k: d[k],reverse=True )])
