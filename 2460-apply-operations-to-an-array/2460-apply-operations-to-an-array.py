class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        zeros=nums.count(0)
        new_s=[x for x in nums if x!=0]
        print(new_s)
        aluti = [0]*zeros
        print(aluti)
        return new_s+aluti
