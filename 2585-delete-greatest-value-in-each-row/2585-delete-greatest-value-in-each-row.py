class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        ans=0
        val=-1
        for i in range(m):
            grid[i].sort()
        print(grid)
        a=n
        while a:
            val=-1
            for i in range(m):
                val=max(val,grid[i][a-1])
            ans+=val
            a-=1

        return ans

        

        
        