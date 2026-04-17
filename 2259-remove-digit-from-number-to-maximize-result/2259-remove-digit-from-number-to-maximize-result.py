class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        num=0
        for i in range(len(number)-1,-1,-1):
            if number[i]==digit:
                num=max(int(number[:i]+number[i+1:]),num)
        return str(num)

        