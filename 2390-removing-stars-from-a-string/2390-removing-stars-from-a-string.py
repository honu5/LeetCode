class Solution:
    def removeStars(self, s: str) -> str:
        t=[]
        for i in s:
            if t and i=="*":
                t.pop()
                
            else: t.append(i)
        return "".join(t)



        