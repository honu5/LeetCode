class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        while n:
            a,b=a+b,a
            n-=1
        return a
        