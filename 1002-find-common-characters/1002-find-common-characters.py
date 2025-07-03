class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans=[]
        word=words[0]
        for i in word:
            found = True
            for j in range(1,len(words)):
                if i not in words[j]:
                    found=False
                words[j]=words[j].replace(i,"",1)
            while(found):
                ans.append(i)
               
                found=False
        return ans
        