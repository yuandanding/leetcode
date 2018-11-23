class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        minind = 2000
        rl = ['1']
        for i in range(0,len(list1)):
            if list1[i] in list2:
                c = list2.index(list1[i])+i
                if c < minind:
                    minind = c
                    rl[-1] = list1[i]
                elif c == minind:
                    rl.append(list1[i])
        return rl