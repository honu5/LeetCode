class Solution:
    def secondHighest(self, s: str) -> int:
        ans=[]
        for i in s:
            if i.isdigit():
                ans.append(int(i))
        ans=list(set(ans))

        ans.sort()
        if len(ans)<=1:
            return -1
        return ans[-2]
        
        