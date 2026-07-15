class Solution:
    def findNthDigit(self, n: int) -> int:
        digit=1
        start=1
        count=9
        while n>digit*count:
            n-=digit*count
            digit+=1
            count*=10
            start*=10
        number=start+(n-1)//digit
        return int(str(number)[(n-1)%digit])
        