class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        string=''
        val=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                found=True
               
                for k in s[i:j+1]:
                    if (k==k.lower() and k.upper() not in s[i:j+1]) or (k==k.upper() and k.lower() not in s[i:j+1]):
                        found=False
                        break
                    
                        
                if found and len(s[i:j+1])>val:
                    
                    string=s[i:j+1]
                    val=len(s[i:j+1])
                print(string)
        return string

        