class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        val=1
        if n==0:
            return 0
        while n:
            val*=n
            n-=1
        
        ret=list(str(val))
        vals=0
        for i in range(len(ret)-1,-1,-1):
            if  ret[i]!='0':
                break
            else:
                vals+=1
        return vals


        