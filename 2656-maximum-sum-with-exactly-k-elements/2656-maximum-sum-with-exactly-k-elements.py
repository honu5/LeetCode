class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        val=0
        for i in range(nums[-1],nums[-1]+k):
            val+=i
        return val
        