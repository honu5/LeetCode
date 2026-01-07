class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        ans=[]
        for i in grid:
            ans.extend(i)
        ans.sort()
        for i in ans:
            if i>=0:
                break
            count+=1
        return count
        