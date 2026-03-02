class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        val=0
        if n<=k and m<=k: 
            return 0
        if k<n:
            val+=(k*(n-k))
        if k<m:
            val+=(k*(m-k))
        return val
        