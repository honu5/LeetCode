class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ugly=[2,3,5]
        if n<1:
            return False
        for i in ugly:

            while n%i==0:
                n//=i
        if n==1:
            return True
        return False
        