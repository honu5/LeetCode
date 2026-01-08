class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        count=Counter(words1)
        counts=Counter(words2)
        val=0
        for i in words1:
            if i in words2 and count[i]==1 and counts[i]==1:
                val+=1
        return val
        