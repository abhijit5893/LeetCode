#https://leetcode.com/problems/shuffle-string/
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        out =[''] * len(s)
        for i,v in enumerate(indices): out[v] = s[i]
        return ''.join(out)