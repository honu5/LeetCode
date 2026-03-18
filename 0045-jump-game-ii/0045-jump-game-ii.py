class Solution:

    def jump(self, nums: List[int]) -> int:
        val=0
        far=0
        end=0

        for curr in range(len(nums)-1):
            far=max(far,curr+nums[curr])
            if curr==end:
                val+=1
                end=far
        return val

        
        