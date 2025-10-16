class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=[]
        for i in range(len(s)):
            ans.append(s[i])
            if len(ans)>=2 and ans[len(ans)-2:]==["A","B"] or ans[len(ans)-2:]==["C","D"]:
                ans.pop()
                ans.pop()
        return len(ans)
            
        