class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        ans=[]
        for i in s:
            if ans and  i == ']':
                if ans[-1]!='[':
                    return False
                else:
                    ans.pop()
        
            elif ans and  i == ')':
                if ans[-1]!='(':
                    return False
                else:
                    ans.pop()
            elif ans and i=='}':
                if ans[-1]!='{':
                    return False
                else:
                    ans.pop()
            else:
                ans.append(i)
        return not ans