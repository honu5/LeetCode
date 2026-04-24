class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if int(num[i])!=int(num.count(str(i))):
                
                return False
        return True
