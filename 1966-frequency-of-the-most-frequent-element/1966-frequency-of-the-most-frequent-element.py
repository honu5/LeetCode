class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        l=0
        total=0
        res=1
        for i in range(1,len(nums)):
            total+=(nums[i]-nums[i-1])*(i-l)
            while total>k:
                total-=nums[i]-nums[l]
                l+=1
            res=max(res,i-l+1)
        return res
