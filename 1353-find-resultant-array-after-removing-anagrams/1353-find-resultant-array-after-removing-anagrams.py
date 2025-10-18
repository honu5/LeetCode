class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        n=len(words)
        i=1
        
        while i<n:
            
            if sorted(list(words[i]))==sorted(list(words[i-1])):
                words.pop(i)
                n-=1
                i-=1
            i+=1
            print(words)
        return words
