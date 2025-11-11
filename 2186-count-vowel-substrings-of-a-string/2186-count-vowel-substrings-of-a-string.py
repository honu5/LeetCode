class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowel=set("aieou")
        count=0
        n=len(word)

        for i in range(n):
            sett=set()
            for j in word[i:]:
                if j not in vowel:
                    break
                sett.add(j)
                if len(sett)==5:
                    count+=1
        return count
