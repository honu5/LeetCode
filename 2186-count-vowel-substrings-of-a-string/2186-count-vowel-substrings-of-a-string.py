class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels=set("aeiou")
        count=0
        n=len(word)
        for i in range(n):
            sett=set()
            for j in word[i:]:
                if j not in vowels:
                    break
                sett.add(j)
                print(sett)
                if len(sett)>=5:
                    count+=1
        return count
        