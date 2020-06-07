# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = collections.defaultdict(list)
        for i, v in enumerate(nums):
            table[v].append(i)

        for i in nums:
            if i != target - i:
                if table.get(i, None) is not None and table.get(target - i, None) is not None:
                    return [table[i][0], table[target - i][0]]
            else:
                if table.get(i, None) is not None:
                    if len(table[i]) > 1:
                        return [j for j in table[i]]

        return []

        '''
        d = {}
        for i,num in enumerate(nums):
            if target-num in d:
                return [i, d[target-num]]
            else:
                d[num]=i
        return []
        '''
