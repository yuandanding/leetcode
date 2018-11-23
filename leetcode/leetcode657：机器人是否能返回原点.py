class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        r = moves.count('R')-moves.count('L')
        l = moves.count('U')-moves.count('D')
        if r == 0 and l==0:
            return True
        return False