#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                candies[i] = True
            else:
                candies[i] = False
        return candies