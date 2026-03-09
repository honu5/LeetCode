class Solution:
    def countEven(self, num: int) -> int:
        n=0
        for i in range(1,num+1):
            val=0
            for j in  str(i):
                val+=int(j)
            if val%2==0:
                n+=1
        return n      