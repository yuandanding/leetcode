class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nu = sorted(nums)
        l = 0
        r = len(nums)-1
        while l <= r:
            if nu[l] == nums[l]:
                l += 1
            elif nu[r] == nums[r]:
                r -= 1
            else:
                break
        if r<=l:
            return 0
        return r-l+1