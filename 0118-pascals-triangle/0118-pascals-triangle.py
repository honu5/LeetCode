class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[[1]]
        for i in range(1,numRows):
            prev=ans[-1]
            rows=[1]
            for j in range(1,i):
                rows.append(prev[j-1]+prev[j])
            rows.append(1)
            ans.append(rows)
        return ans
