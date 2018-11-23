class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                if i == 0 or nums[i-1]<=nums[i+1]:
                    count+=1
                elif i == len(nums)-2 or nums[i]<=nums[i+2]:
                    count+=1
                else:
                    return False
            if count > 1:
                return False
        return True
        