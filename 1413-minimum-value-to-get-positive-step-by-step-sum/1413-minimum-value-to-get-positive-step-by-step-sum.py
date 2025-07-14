class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minSum=0
        curSum=0
        for num in nums:
            curSum+=num
            minSum=min(curSum,minSum)
        return 1-minSum