class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ=0
        prod=1
        for i in str(n):
            summ+=int(i)
            prod*=int(i)
        total=summ+prod
        return True if n%total==0 else False
        
        