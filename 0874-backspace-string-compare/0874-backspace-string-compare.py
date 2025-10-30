class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        ans=[]
        for i in s:
            if ans and i=="#":
                ans.pop()
            else:ans.append(i)
        t=list(t)
        ans1=[]
        for i in t:
            if ans1 and i=="#":
                ans1.pop()
            else:ans1.append(i)
        print(ans,ans1)
        for i in ans1:
            if i=="#":
                ans1.remove(i)
        for i in ans:
            if i=="#":
                ans.remove(i)
        if ans==ans1:
            return True
        return False
        
        