class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s=str(n)
        y=str(x)
        if y in s and not s.startswith(y):
            return True
        return False
        