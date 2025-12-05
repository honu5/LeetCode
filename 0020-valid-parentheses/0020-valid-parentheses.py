class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans=[]
        if len(s)==1 or s[0] in [")","]","}"]:
            return False
        for i in s:
            if i=="]":
                if not ans or ans[-1]!="[":
                    return False
                ans.pop()
            elif i==")":
                if not ans or ans[-1]!=  "(":
                    return False
                ans.pop()
            elif i=="}":
                if not ans or ans[-1]!= "{":
                    return False
                ans.pop()
            else:
                ans.append(i)
        if ans:
            return False
        return True
                