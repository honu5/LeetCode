class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        val=0
        for i in words:
            if i.startswith(pref):
                val+=1
        return val
        