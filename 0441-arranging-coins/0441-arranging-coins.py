class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt=0
        if n==1:
            return 1
        for  i in range(1,n+1):
            a=i*(i+1)/2
            cnt+=1
            if a>n:
                break
        return cnt-1
        