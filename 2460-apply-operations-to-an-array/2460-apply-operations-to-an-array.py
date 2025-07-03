class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)-1
        for i in range(n):
            if nums[i]==nums[i+1]:
                nums[i],nums[i+1]=nums[i]*2,0
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
        return nums
                

        

        
        