class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans=[]
        s1=s1.split(" ")
        s2=s2.split(" ")
        count=Counter(s1)
        count2=Counter(s2)
        for i in s1:
            if i not in s2 and i not in ans and count[i]==1:
                ans.append(i)
        for i in s2:
            if i not in s1 and i not in ans and count2[i]==1:
                ans.append(i)
        return ans
        