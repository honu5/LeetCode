class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=[]
        for i in s:
            if ans and i.isdigit():
                ans.pop()
            else:
                ans.append(i)
        return ''.join(ans)

        