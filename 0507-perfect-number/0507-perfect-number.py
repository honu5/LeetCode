class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num%2==1:
            return False
        ans=1
        for i in range(2,int(sqrt(num))+1):
            if num%i==0 :
                ans+=(i+num/i)
        return ans==num

        