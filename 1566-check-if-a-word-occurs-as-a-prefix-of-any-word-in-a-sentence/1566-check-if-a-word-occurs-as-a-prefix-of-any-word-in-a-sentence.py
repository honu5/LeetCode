class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        s=sentence.split()
        for i in s:
            if i.startswith(searchWord):
                return s.index(i)+1
        return -1
        