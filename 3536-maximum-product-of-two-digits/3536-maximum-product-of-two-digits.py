class Solution:
    def maxProduct(self, n: int) -> int:
        lst=list(str(n))
        lst.sort()
        return int(lst[-1])*int(lst[-2])
        