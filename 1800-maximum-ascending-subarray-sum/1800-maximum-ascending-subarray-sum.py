class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums==sorted(nums)[::-1]:
            return max(nums)
        summ=nums[0]
        val=nums[0]

        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                val=nums[i]
            else:
                val+=nums[i]
            summ=max(val,summ)
        return summ



        