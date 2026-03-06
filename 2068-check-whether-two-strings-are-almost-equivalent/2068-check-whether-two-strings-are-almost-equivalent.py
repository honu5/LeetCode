class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1=Counter(word1)
        count2=Counter(word2)
        for i in count1:
            if  abs(count1[i]-count2[i])>3:
                return False
        for i in count2:
            if  abs(count1[i]-count2[i])>3:
                return False
        return True
        