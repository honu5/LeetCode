class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        val=0
        n=len(forts)
        
        for i in range(len(forts)-1):
            if forts[i]==1:
                sl=i+1
                while sl<n and forts[sl]==0 :
                    sl+=1
                if sl<n and forts[sl]==-1:
                    vals=sl-i-1
                    val=max(val,vals)
            

            if forts[i]==-1:
                sl=i+1
                while sl<n and  forts[sl]==0:
                    sl+=1
                if sl<n and forts[sl]==1:
                    vals=sl-i-1
                    val=max(val,vals)
                    
        return val
            
        