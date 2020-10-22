#https://leetcode.com/problems/palindrome-partitioning/
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def palindrome(s, path):
            if not s:
                res.append(path)
            for i in range(len(s)):
                if s[:i+1] == s[:i+1][::-1]:
                    palindrome(s[i+1:],path+[s[:i+1]])

        res = []
        palindrome(s, [])
        return res

