class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        if nums[-1]-nums[0]<=2*k:
            return 0
        else: return nums[-1]-nums[0]-2*k
        