class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(x:int)->bool:
            y=int(x**0.5)
            return y*y==x
        if is_square(n):
            return 1
        while n%4==0:
            n//=4
        if n%8==7:
            return 4
        i=1
        while i*i<=n:
            if is_square((n-(i*i))):
                return 2
            i+=1
        return 3
        