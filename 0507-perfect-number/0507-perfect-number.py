class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num%2==1:
            return False
        ans=1
        lst=[]
        for i in range(2,int(sqrt(num))+1):
            if num%i==0 and i not in lst:
                ans+=(i+num/i)
                lst.append(num/i)
                #print(i,num/i,ans)
        return ans==num

        