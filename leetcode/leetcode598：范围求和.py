class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == []:
            return m*n
        i = []
        j = []
        for op in ops:
            i.append(op[0])
            j.append(op[1])
        ri = min(i) * min(j)
        return min(ri,m*n)
        