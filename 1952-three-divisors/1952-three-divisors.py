class Solution:
    def isThree(self, n: int) -> bool:
        val=False
        for i in range(2,n):
            if val and n%i==0:
                return False
            if n%i==0:
                val=True
        return val
        