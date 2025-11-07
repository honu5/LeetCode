class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        l=0
        r=len(s)-1
        s=list(s)
        while l<r:
            if not s[l].isalpha():
                l+=1
            elif not s[r].isalpha():
                r-=1
            else:
                val=s[l]
                s[l]=s[r]
                s[r]=val
                l+=1
                r-=1
        return "".join(s)
        