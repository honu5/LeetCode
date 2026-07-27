class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx=nums[0]
        minn=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxx,minn=minn,maxx
            maxx=max(nums[i],maxx*nums[i])
            minn=min(nums[i],minn*nums[i])

            ans=max(ans,maxx)
        return ans
        