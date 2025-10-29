class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if len(str(x))==1:
            return True
        n=len(str(x))
        l=0
        r=n-1
        while l<=r:
            if str(x)[l]!=str(x)[r]:
                return False
            l+=1
            r-=1
        return True

        