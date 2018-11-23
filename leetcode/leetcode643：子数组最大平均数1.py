class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        su = 0
        maxsu = -100000
        for i in range(0,len(nums)):
            su += nums[i]
            if i >= k:
                su -= nums[i-k]
            if i >= k-1:
                maxsu = max(su/k,maxsu)
        return maxsu