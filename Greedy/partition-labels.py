#https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        output = []
        last = {c:i for i,c in enumerate(S)}
        print(last)
        start, end = 0, 0
        for i in range(len(S)):
            end = max(end,last[S[i]])
            if  i == end:
                output.append(end-start+1)
                start =  i + 1
        return output