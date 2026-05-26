class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def helper(x):
            return not '0' in str(x)
        for i in range(1,n):
            j=n-i
            if helper(i) and helper(j):
                return [i,j]
        