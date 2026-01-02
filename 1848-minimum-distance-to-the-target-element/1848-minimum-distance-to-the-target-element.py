class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        n=len(nums)
        for i in range(len(nums)):
            if target==nums[i]:
                val=abs(i-start)
                n=min(n,val)
        return n
        
        