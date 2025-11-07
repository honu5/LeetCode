class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        t=""
        n=min(len(word1),len(word2))
        while n:
            t+=word1[i] 
            t+=word2[i]
            i+=1
            n-=1
        if len(word1)<len(word2):
            t+=word2[len(word1):]
        else:
            t+=word1[len(word2):]

        return t
        