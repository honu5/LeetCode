class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        m=1
        while m<n:
            m=(2**a)-1
            a+=1
        return m

        