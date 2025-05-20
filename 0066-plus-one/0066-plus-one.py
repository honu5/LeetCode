class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stri=""
        for i in digits:
            stri+=str(i)
        num=int(stri)+1
        lst= [int(x)  for x in str(num)]
        return lst