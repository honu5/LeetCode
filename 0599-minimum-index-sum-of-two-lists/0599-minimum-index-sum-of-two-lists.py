class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans=[]
        for i in list1:
            if i in list2:
                ans.append(i)
        if len(ans)==1:
            return ans
        print(ans)
        m=len(list1)+len(list2)+1
        anss=[1]
        for i in ans:
            
            val=list1.index(i)+list2.index(i)
            print(m,val)
            if val<m:
                anss.pop()
                anss.append(i)
                m=val
            elif val==m:
                anss.append(i)                
        return anss

        
                
        

        
        