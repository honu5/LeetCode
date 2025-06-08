class Solution:
    def isPalindrome(self, x: int) -> bool:
        strg=str(x)
        l=0
        r=len(strg)-1
        while l<r:
            if strg[l]!=strg[r]:
                return False
            l+=1
            r-=1
        return True