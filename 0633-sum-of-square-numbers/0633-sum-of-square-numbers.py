class Solution:
    def judgeSquareSum(self, c: int) -> bool:
       
        l=0
        r=int(c**0.5)
        
        while l<=r:
            squar=((l**2) + (r**2))
            
            if squar==c:
                return True
                l+=1
                r-=1
            elif squar < c:
                l+=1
            else : r-=1
        return False

        





''' if c==0:
            return 0
        if (c**0.5)%2==0:
            cnt+=1'''