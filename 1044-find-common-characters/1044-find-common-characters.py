from collections import Counter

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common = Counter(words[0])
        
        for w in words[1:]:
            common &= Counter(w)
        
        ans = []
        for ch, freq in common.items():
            ans.extend([ch] * freq)
        
        return ans
