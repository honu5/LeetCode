class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''profit=0
        
        for i in range(len(prices)-1):
            
            if prices[i]<prices[i+1]:
                if prices[i]==min(prices):
                    return max(profit,max(prices[i:])-prices[i])
                else:
                    val=max(prices[i:])-prices[i]
            else:continue
            profit=max(profit,val)
        return profit'''

        '''profit=0
        l=0
        
        r=len(prices)-1
        while (l<r):
            if prices.index(min(prices))<prices.index(max(prices)):
                return max(prices)-min(prices)
            if prices[l]>=prices[l+1]:
                l+=1
            elif prices[r]<=prices[r-1]:
                r-=1
            elif prices[l]<prices[l+1]:
                profit=max(profit,prices[r]-prices[l],prices[l+1]-prices[l])
                l+=1
            else:
                profit=max(profit,prices[r]-prices[l],prices[r]-prices[r+1])
                r-=1
        return profit'''
        '''nums=sorted(prices)
        idx=[]
        for i in nums:
            idx.append(prices.index(i))
        l=0
        r=len(idx)-1'''
        
        min_price=float("inf")
        max_profit=0
        for i in prices:
            min_price=min(min_price,i)
            max_profit=max(max_profit,i-min_price)
        return max_profit



        