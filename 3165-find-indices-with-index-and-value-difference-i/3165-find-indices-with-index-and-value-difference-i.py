class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        l=0
        while l<len(nums):
            r=l+indexDifference
            for i in range(r,len(nums)):
                if abs(nums[i]-nums[l])>=valueDifference:
                    return [l,i]
            l+=1
        return [-1,-1]