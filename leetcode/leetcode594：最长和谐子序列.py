class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nu = collections.Counter(nums)
        ma = 0
        for n in nu:
            if n+1 in nu:
                ma = max(nu[n]+nu[n+1],ma)
        return ma