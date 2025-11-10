class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        s=str(num)
        val=0
        for i in range(len(s)+1-k):
            x=int(s[i:i+k])
            if x!=0 and  num%x==0:
                val+=1
        return val
        