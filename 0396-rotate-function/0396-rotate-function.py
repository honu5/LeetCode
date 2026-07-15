class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        val=0
        n=len(nums)
        total=sum(nums)
        for i in range(len(nums)):
            val+=(i*nums[i])
        vals=val
        for i in range(n-1,0,-1):
            val=val+total-n*nums[i]
            vals=max(val,vals)
        return vals
         
        