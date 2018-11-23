class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """ 
        
        m = str(abs(x))
        s = int( m[::-1])
        if (s < -2147483648) or (s > 2147483648):
            return 0
        if x < 0 :
            s=-1*s
        return(s)
        
