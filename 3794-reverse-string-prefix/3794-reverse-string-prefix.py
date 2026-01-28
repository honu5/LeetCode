class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lst=list(s[0:k])
        lst1=s[k:]
        rvrsd=lst[::-1]
        lstt=''.join(rvrsd)
        return lstt+lst1