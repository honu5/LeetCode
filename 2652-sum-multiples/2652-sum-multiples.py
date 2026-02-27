class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        val=0
        if n<3:
            return 0
        for i in range(3,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                val+=i
        return val
        