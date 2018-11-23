class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        s = set(nums)
        su = int((1+n)*n/2)
        es = sum(nums) - sum(s)
        ss = su - sum(s)
        return [es,ss]