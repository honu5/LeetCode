class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(prices)-1):
            found=False
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    ans.append(prices[i]-prices[j])
                    break
                if j==len(prices)-1:
                    ans.append(prices[i])
        ans.append(prices[-1])
        return ans


        