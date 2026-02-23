class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        val=0
        i=1

        while n>0:
            n-=i
            i+=1
            val+=1
        if n==0:
            return val
        else: return val-1

        