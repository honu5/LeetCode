class Solution:
    def isHappy(self, n: int) -> bool:
        listt=[]
        while True:
            st=str(n)
            r=0
            for i in st:
                r+=int(i)**2
            if r==1:
                return True
            elif r in listt:
                return False
            listt.append(r)
            n=r