class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        '''ad=0
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
        return False'''
        total=1
        if num%2!=0:
            return False
        

        for i in range(2,int(sqrt(num))+1):
            if num%i==0:            
                total+=i
                if i!=num/i:
                    total+=num/i
                
        
        
        if total==num:
            return True
        return False

        