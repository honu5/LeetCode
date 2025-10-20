class Solution(object):
    def maxCoins(self, piles):
        
        n=len(piles)
        piles.sort()
        m=n-2
        t=len(piles)//3
        ans=0

        for i in range(m,t-1,-2):
            ans+=piles[i]

        return ans

