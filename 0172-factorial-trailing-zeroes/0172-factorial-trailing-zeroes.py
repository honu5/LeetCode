class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ns=0
        while n:
            
            ns+=(n//5)
            n//=5
            
        return ns

        