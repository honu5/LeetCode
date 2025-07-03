class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        idx=0
    
        for i in range(n):
            if i<n-1 and  nums[i]==nums[i+1]:
                nums[i],nums[i+1]=nums[i]*2,0
            if nums[i]!=0:
                nums[i],nums[idx]=nums[idx],nums[i]
                idx+=1
            

        
        return nums
                

        

        
        