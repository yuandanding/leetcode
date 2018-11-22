class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        tag = 0
        s=s.upper()
        st = []
        for a in s:
            if a.isalpha() or a.isdigit():
                st.append(a)
        for i in range(0,int(len(st)/2)):
            if st[i] != st[-1-i]:
                tag = 1
                return False
        if tag == 0:
            return True