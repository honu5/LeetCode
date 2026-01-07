class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        ans=[]
        words.sort(key=len)
        print(words)
        for i in range(len(words)):
            for j  in range(i+1,len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans
        