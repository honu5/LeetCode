class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        val=0
        word=list(set(word))
        for i in word:
            if i.islower() and i.upper() in word:
                val+=1
        return val
        