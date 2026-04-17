class Solution:
    def maxDistance(self, c: List[int]) -> int:
        n=len(c)
        ans=-1
        for i in range(n-1):
            for j in range(n-1,i,-1):
                if c[i]!=c[j]:
                    if j-i>=ans:
                        ans=j-i
                    break
        return ans

        