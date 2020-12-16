#https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(n,k,1,res,[])
        return res
    def dfs(self,n,k,idx,res,path):
        if len(path) == k and path not in res:
            res.append(path)
        for i in range(idx,n+1):
            self.dfs(n,k,i+1,res,path+[i])

