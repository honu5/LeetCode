class Solution(object):
    def maxCoins(self, piles):
        
        piles.sort()
        m=len(piles)-2
        t=len(piles)//3
        ans=[]

        for i in range(m,t-1,-2):
            ans.append(piles[i])

        return sum(ans)

