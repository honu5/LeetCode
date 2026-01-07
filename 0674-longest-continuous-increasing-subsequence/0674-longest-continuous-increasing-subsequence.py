class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=1
        counter=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                l+=1
                counter=max(counter,l)
            else:
                l=1
        return counter
        