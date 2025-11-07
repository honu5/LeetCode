class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        n=len(s)
        ans=[]
        while i<n:
            cnt=1
            while i+1<n and  s[i]==s[i+1]:
                cnt+=1
                i+=1
            ans.append(cnt) 
            i+=1
        val=0
        for i in range(1,len(ans)):
            val+=min(ans[i],ans[i-1])
        return val


        