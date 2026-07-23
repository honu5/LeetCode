class Solution:
    def merge(self, inr: List[List[int]]) -> List[List[int]]:
        inr.sort()
        n=len(inr)
        ans=[]
        prev=inr[0]
        for i in range(1,n):
            if inr[i][0]<=prev[1]:
                prev[1]=max(inr[i][1],prev[1])
            else:
                ans.append(prev)
                prev=inr[i]
        
        ans.append(prev)
        return ans



        