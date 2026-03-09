class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ans=[]
        if s1==s2:
            return True
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                ans.extend([i])
        print(ans)
        if len(ans)!=2:
            return False
        return (s1[ans[0]]==s2[ans[1]] and s2[ans[0]]==s1[ans[1]])
        
            

        