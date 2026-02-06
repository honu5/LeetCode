class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=list(s)
        for i in range(len(lst)):
            if lst[i].islower():
                continue
            lst[i]=lst[i].lower()
        return "".join(lst)
        