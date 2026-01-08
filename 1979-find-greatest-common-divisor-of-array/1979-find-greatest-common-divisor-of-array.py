class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1,nums[0]+1):
            if nums[-1]%i==0 and nums[0]%i==0:
                val=i
        return val
        