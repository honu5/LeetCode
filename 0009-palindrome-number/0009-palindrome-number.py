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
        

        if str(x)==str(x)[::-1]:
            return True
        print(str(x),reversed(str(x)))
        
        return False
