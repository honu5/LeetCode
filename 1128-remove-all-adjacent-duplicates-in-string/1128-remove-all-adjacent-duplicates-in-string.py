class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=[]
        for i in s:
            if ans and ans[-1]==i:
                ans.pop()
            else:ans.append(i)
        return ''.join(ans)
        