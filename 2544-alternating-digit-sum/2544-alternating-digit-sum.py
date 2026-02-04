class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        val=0
        num=str(n)
        for i in range(len(num)):
            if i%2==0:
                val+=int(num[i])
            else:
                val-=int(num[i])
        return val


        