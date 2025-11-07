class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''if not s:
            return 0
        val=s[0]
        l=0
        r=1
        ans=1
        n=len(s)
        

        while r<len(s):
            
            if s[r] in val:
                l = l + val.index(s[r]) + 1
                val = s[l:r+1]  
            else:
                val+=s[r]
                r+=1
                ans=max(ans,len(val))
                
           
        return ans'''
        if len(s)==1:
            return 1

        s=list(s)
        l=0
        r=1
        val=0
        
        
        while r<len(s):
            slced=s[l:r+1]
            if len(slced)==len(set(slced)):
                val=max(val,len(slced))
                r+=1
            else:
                l+=1
        return val
            

        