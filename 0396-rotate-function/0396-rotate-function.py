class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        val=0
        total=sum(nums)
        n=len(nums)
        for i in range(n):
            val+=i*nums[i]
        vals=val
        for i in range(n-1,0,-1):
            val=val+total-n*nums[i]
            vals=max(vals,val)
        return vals