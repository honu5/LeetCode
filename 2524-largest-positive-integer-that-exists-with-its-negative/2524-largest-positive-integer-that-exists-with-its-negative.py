class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0]>0:
            return -1
        r=len(nums)-1

        for i in range(r,-1,-1):
            print(i)
            if nums[i]<0:
                break
            if -nums[i] in nums:
                return nums[i]
        return -1

