class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        string=str(num)
        val=0
        for i in string:
            if num%int(i)==0:
                val+=1
        return val
        