#https://leetcode.com/problems/count-items-matching-a-rule/
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count =0
        idx = 0
        if ruleKey =='color': idx = 1
        elif ruleKey == 'name': idx = 2
        for i in items:
            if i[idx] == ruleValue:
                count += 1
        return count