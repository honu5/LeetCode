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
        
        final=0
        for i in range(len(ans)):
            additionalRocks-=ans[i]
            if additionalRocks<0:
                return i
                
            

        return len(ans)
            
        