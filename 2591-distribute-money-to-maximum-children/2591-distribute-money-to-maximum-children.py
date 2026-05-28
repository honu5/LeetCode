class Solution:
    def distMoney(self, m: int, c: int) -> int:

        rem=m-c
        if rem<0:
            return -1
        if (rem//7==c) and (rem%7==0):
            return c
        if (rem//7==c-1 and rem%7==3 ):
            return c-2
        return min(c-1,rem//7)
        