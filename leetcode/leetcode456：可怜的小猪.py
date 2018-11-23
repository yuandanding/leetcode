class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets == 1:
            return 0
        m = int(minutesToTest/minutesToDie)+1
        cm = m
        count = 1
        while cm < buckets:
            cm = cm*m
            count += 1
        return count
