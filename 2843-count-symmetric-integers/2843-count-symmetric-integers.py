class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        i=low
        val=0
        while i<=high:
            if len(str(i))%2==1:
                s='1'+(len(str(i))*'0')
                i=int(s)
            else:
                n=len(str(i))//2
                if sum(list(map(int,str(i)[:n])))==sum(list(map(int,str(i)[n:]))):
                    val+=1
                i+=1
            
        return val
            
        