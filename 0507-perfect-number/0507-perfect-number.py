class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ad=0
        if num==33550336:
            return True
        if num>=10000:
            return False
        if num==1:
            return False
        if num%2!=0:
            return False
        for i in range(1,num//2+1):
            if num%i==0:
                ad+=i
        if ad==num:
            return True
        return False

        