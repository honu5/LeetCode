class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        y=[a[0] for a in coordinates]
        b=[a[1] for a in coordinates]
        if len(set(y))==1 or len(set(b))==1:
            return True
        if len(set(y))!=len(y) or len(set(b))!=len(b):
            return False
       
        if len(coordinates)==2:
            return True
        slp=(float(coordinates[1][1])-float(coordinates[0][1]))/(float(coordinates[1][0])-float(coordinates[0][0]))
        for i in range(2,len(coordinates)):
            if ((float(coordinates[i][1])-float(coordinates[0][1]))/(float(coordinates[i][0])-float(coordinates[0][0])))!=slp:
                return False
        return True
        