class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l=0
        r=0
        
        while l<len(s):
            found=False
            for i in range(r,len(t)):
                if s[l]==t[i]:
                    found=True
                    r=i+1
                    break
            if not found:
                    return False
            l+=1
        return True

        