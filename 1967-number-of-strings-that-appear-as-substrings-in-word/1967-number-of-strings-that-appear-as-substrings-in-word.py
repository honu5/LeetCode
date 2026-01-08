class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        val=0
        for i in patterns:
            if i in word:
                val+=1
        return val
        