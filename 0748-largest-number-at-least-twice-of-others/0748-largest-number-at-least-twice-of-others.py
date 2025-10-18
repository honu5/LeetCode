class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=sorted(nums)
        if num[-1]>=num[-2]*2:
            return nums.index(num[-1])
        return -1
        