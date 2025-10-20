class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n=len(piles)
        piles.sort()
        l,m=0,n-2
        ans=0

        while l<m:
            ans+=piles[m]
            l+=1
            m-=2

        return ans

