class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        arr=[[rocks[i],capacity[i]] for i in range(len(rocks))]
        ans=[]
        for i in arr:
            ans.append(i[1]-i[0])
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
            
        