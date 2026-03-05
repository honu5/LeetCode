class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        '''count1=Counter(s)
        count2=Counter(t)
        most1=count1.most_common()
        most2=count2.most_common()
        if len(most1)!=len(most2):
            return False
        for i in range(len(most1)):
            if most1[i][1]!=most2[i][1]:
                return False
        return True'''
        for i in range(len(s)):
            if s.index(s[i])!=t.index(t[i]):
                return False
        return True
        