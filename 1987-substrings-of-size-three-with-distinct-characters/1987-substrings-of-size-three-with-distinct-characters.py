class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        count=0
        for i in range(len(s)-2):
            wndw=s[i:i+3]
            if len(list(wndw))==len(set(wndw)):
                count+=1
        return count


        