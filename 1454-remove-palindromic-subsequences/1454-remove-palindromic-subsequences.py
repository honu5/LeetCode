class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s==s[::-1]:
            return 1
        return 2
        