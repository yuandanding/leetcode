class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(s):
            if len(s) == 1:
                return True
            for i in range(0,int(len(s)/2)):
                if s[i] != s[-1-i]:
                    return False
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            elif isPalindrome(s[i+1:j+1]) or isPalindrome(s[i:j]):
                return True
            else:
                return False
        return True
        