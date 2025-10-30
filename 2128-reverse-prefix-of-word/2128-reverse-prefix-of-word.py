class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word

        word=list(word)
        idx=word.index(ch)
        left=word[0:idx+1]
        right=word[idx+1:]
        retur=left[::-1]+right
        return ''.join(retur)
        