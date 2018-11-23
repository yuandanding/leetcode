class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        r1 = nums[-1] *nums[-2] *nums[-3]
        if nums[-1] >= 0:
            r2 = nums[0] * nums[1] * nums[-1]
        else:
            r2 = nums[0] * nums[1] * nums[2]
        return max(r1,r2)