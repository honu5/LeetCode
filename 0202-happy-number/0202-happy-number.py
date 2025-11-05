class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans=[]
        val=0
        while True:
            val=0
            for i in str(n):
                val+=int(i)**2
                if val in ans:
                    return False
            ans.append(val)
            if val==1:
                return True
            n=val
            
            print(ans)
        
        