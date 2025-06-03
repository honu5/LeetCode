class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[len(nums)-1]<target:
            return len(nums)
        if nums[0]>target:
            return 0
        for i in range(len(nums)-1):
            if nums[i]==target:
                return i
            elif nums[i]<target and nums[i+1]>target:
                return i+1
            else : continue