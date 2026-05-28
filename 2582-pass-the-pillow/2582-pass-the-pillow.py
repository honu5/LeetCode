class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos=1
        if (time//(n-1))%2==1:
            pos=0
        rem=time%(n-1)
        if pos==1:
            return rem+1
        else: return n-rem
       