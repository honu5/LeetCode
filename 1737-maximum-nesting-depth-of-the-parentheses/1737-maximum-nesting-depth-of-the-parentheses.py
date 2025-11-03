class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=[]
        val=0
        for i in s:
            if i=='(':
                ans.append(i)
            elif i==')':
                
                val=max(val,len(ans))
                ans.pop()

            elif i.isdigit():
                val=max(val,len(ans))
        return val