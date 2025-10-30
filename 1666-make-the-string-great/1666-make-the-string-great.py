class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        
        ans=[]
        for i in s:
            if ans and ((ans[-1]!=i and ans[-1].lower()==i) or (ans[-1]!=i and  ans[-1].upper()==i)):
                ans.pop()
            else:ans.append(i)
        return "".join(ans)
        