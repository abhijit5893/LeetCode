#771. Jewels and Stones

'''
Hash Table solution
Space - O(m)
Time - O(m+n)
'''
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total_jewels = 0
        stones_map = collections.defaultdict()
        if len(jewels) and len(stones):
            for stn in jewels:
                stones_map[stn] = 1
            for stn in stones:
                if stones_map.get(stn, None) is not None:
                    total_jewels += 1
        return total_jewels


# if __name__=="__main__": 
#     sol = Solution()
#     jewels = "aA"
#     stones = "aAAbbbb"
#     print(sol.numJewelsInStones(jewels,stones))