class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(M)
        l = len(M[0])
        if r == 0 or l == 0 or(r ==1 and l ==1):
            return M
        if r == 1:
            rl = []
            r2 = []
            rl.append(int((M[0][0]+M[0][1])/2))
            for i in range(1,l-1):
                rl.append(int((M[0][i-1]+M[0][i]+M[0][i+1])/3))
            rl.append(int((M[0][l-2]+M[0][l-1])/2))
            r2.append(rl)
            return r2
        elif l == 1:
            rl = []
            r2 = []
            rl.append(int((M[0][0]+M[1][0])/2))
            r2.append(rl)
            rl = []
            for i in range(1,r-1):
                rl.append(int((M[i-1][0]+M[i][0]+M[i+1][0])/3))
                r2.append(rl)
                rl = []
            rl.append(int((M[r-2][0]+M[r-1][0])/2))
            r2.append(rl)
            return r2
        list1 = []
        list2 = []
        count = 0
        for i in range(0,r):
            for j in range(0,l):
                if i == 0 and j == 0:
                    n = int((M[0][1]+M[1][0]+M[1][1]+M[0][0])/4)
                elif i == 0 and j == l-1:
                    n = int((M[0][l-2]+M[1][l-1]+M[1][l-2]+M[0][l-1])/4)
                elif i == r-1 and j == 0:
                    n = int((M[r-2][0]+M[r-1][1]+M[r-2][1]+M[r-1][0])/4)
                elif i == r-1 and j == l-1:
                    n = int((M[r-1][l-2]+M[r-2][l-1]+M[r-2][l-2]+M[r-1][l-1])/4)
                elif i == 0:
                    n = int((sum(M[0][j-1:j+2])+sum(M[1][j-1:j+2]))/6)
                elif i == r-1:
                    n = int((sum(M[r-1][j-1:j+2])+sum(M[r-2][j-1:j+2]))/6)
                elif j == 0:
                    n = int((M[i-1][0]+M[i][0]+M[i+1][0]+M[i-1][1]+M[i][1]+M[i+1][1])/6)
                elif j == l-1:
                    n = int((M[i-1][l-1]+M[i][l-1]+M[i+1][l-1]+M[i-1][l-2]+M[i][l-2]+M[i+1][l-2])/6)
                else:
                    n = int((sum(M[i-1][j-1:j+2])+sum(M[i][j-1:j+2])+sum(M[i+1][j-1:j+2]))/9)
                list1.append(n)
                count+=1
                if count == l:
                    list2.append(list1)
                    count = 0
                    list1 = []
        return list2