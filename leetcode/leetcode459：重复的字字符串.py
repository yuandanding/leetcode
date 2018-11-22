class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1,n//2+1):
            if n % i == 0:
                subs = s[:i]
                j = i
                while j < n and s[j:j+i] == subs:
                    j += i
                if j == n:
                    return True
        return False