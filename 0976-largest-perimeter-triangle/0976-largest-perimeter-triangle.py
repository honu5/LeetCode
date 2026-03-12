class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i=len(nums)-1
        while i>=2:
            if nums[i]<(nums[i-1]+nums[i-2]):
                return sum(nums[i-2:i+1])
            else: i-=1
        return 0
        