# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        O(nlogn) with Hash tables and sorting
        '''
        table = dict()
        for i in nums:
            if table.get(i, None) is None:
                table[i] = 1
            else:
                table[i] += 1

        out = [i[0] for i in sorted(table.items(), key=lambda kv: kv[1], reverse=True)]
        return out[:k]

