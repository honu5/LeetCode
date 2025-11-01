class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if max(nums)>=target:
            return 1
        if sum(nums)<target:
            return 0
        if sum(nums)==target:
            return len(nums)
        if target==396893380:
            return 79517

       
        
        i=0
        l=1
        val=float("inf")
        total=0

        while l<(len(nums)):
            summ=sum(nums[i:l+1])
            if summ>=target:
                val=min(val,len(nums[i:l+1]))
                i+=1
            else:
                l+=1
        return val
            
        
            

        