class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sorted(nums)==nums or  sorted(nums)[::-1]==nums:
            return True
        return False
        