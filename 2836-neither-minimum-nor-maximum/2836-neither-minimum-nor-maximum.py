class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return -1
        for i in nums:
            if i!=max(nums) and i!=min(nums):
                return i
        
        
        