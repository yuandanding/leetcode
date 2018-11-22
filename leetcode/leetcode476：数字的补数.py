class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = ''
        n = bin(num)
        for i in n:
            if i == '0':
                l+='1'
            else:
                l+='0'
        p = int(l[1:],2)
        return p