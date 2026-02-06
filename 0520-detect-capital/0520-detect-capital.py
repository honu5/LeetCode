class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)==1:
            return True
        all=False
        first=False
        allS=False
        if word[0].islower():
            allS=True
        if word[0].isupper():
            if word[1].isupper():
                all=True
            else:
                first=True
        for i in range(1,len(word)):
            if all and word[i].islower():
                return False
            if first and word[i].isupper():
                return False
            if allS and word[i].isupper():
                return False
        return True
        
            
        