class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        rn = 0
        count = 1
        for i in range(0,len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                rn = max(rn,count)
                count = 1
        rn = max(rn,count)
        return rn
        