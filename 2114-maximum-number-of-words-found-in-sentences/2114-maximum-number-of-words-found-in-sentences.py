class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ans=[]
        for i in sentences:
            count=Counter(i)
            ans.append(count[" "])
        return max(ans)+1

        