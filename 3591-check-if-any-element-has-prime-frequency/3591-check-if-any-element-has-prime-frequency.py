class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def prime(n):
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        count=Counter(nums)
        for i in count.values():
            if i>1 and prime(i):
                return True
        return False
        