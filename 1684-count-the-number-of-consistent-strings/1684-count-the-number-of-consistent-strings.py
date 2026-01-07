class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        for i in words:
            f=True
            for j in i:
                if not j in allowed:
                    f=False
                    continue
            if f:
                count+=1
        return count
        