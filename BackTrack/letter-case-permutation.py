#https://leetcode.com/problems/letter-case-permutation/
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res =[]
        self.dfs(S, len(S), 0, res, '')
        return res
    def dfs(self, S, n, idx, res, word):
        if idx == n and len(word) == n and word not in res:
            res.append(word)
        for i in range(idx,n):
            self.dfs(S,n,i+1,res,word+str.upper(S[i]))
            self.dfs(S,n,i+1,res,word+str.lower(S[i]))