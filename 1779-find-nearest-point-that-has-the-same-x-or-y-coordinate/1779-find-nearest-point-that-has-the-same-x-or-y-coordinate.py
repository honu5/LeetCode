class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        ans=[]
        val=float('inf')
    
        for i in points:
            if i[0]==x or i[1]==y:
                ans.append(i)
        if not ans:
            return -1
        
        for i in ans:
            vals=abs(i[0]-x)+abs(i[1]-y)
            if vals<val:
                final=i
            val=min(vals,val)
        return points.index(final)
        