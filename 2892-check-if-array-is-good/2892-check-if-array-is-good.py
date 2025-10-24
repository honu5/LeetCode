class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)-len(set(nums))>=2:
            return False
        if len(nums)==1:
            return False
        nums.sort()
       
        if nums[-1] == len(nums)-1 and  nums[-2] == len(nums)-1:
            
            return True
        
        return False
        