class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        m = len(houses)
        n = len(heaters)
        minr = 0
        j = 0
        for i in range(0,m):
            while j< n-1 and abs(heaters[j] - houses[i]) >= abs(heaters[j+1] - houses[i]):
                j += 1
            minr = max(minr,abs(heaters[j] - houses[i]))
        return minr