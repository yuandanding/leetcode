class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        l = 0
        r = int(pow(c,0.5))
        while l <= r:
            m = l**2 + r**2
            if m == c:
                return True
            elif m < c:
                l += 1
            else:
                r -= 1
        return False