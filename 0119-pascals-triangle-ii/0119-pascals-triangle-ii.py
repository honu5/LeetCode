class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans=[[1]]
        for i in range(1,rowIndex+1):
            prev=ans[-1]
            rows=[1]
            for j in range(1,i):
                rows.append(prev[j-1]+prev[j])
            rows.append(1)
            ans.append(rows)
        return ans[rowIndex]
        