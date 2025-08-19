class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n=len(needle)
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                print(haystack[i:n])
                if haystack[i:i+n]==needle:
                    return i
        