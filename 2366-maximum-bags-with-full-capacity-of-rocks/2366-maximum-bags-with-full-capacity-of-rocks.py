class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        
        ans=[]
        for i in range(len(rocks)):
            ans.append(capacity[i]-rocks[i])
        ans.sort()
        i=0
        final=0
        while additionalRocks and i<len(ans):
            additionalRocks-=ans[i]
            if additionalRocks<0:
                break
            
            
            i+=1
            final+=1
        return final
            
        