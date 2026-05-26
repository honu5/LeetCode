class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        val=0
        while num:
            if num%2==0:
                num//=2
            else: num-=1
            val+=1
        return val
        