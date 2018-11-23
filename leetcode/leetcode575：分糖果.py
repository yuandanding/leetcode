class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        n = len(candies) // 2
        c = set(candies) 
        return min(n,len(c))
        