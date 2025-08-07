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
        if num <= 1:
            return False
    
        total = 1  # 1 is always a divisor (except for 1 itself)
        sqrt_n = int(math.sqrt(num))
        
        for i in range(2, sqrt_n + 1):
            if num % i == 0:
                total += i
                if i != num // i:  # Avoid adding square root twice
                    total += num // i
        
        return total == num