class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target<=nums[0]:
            return 0
        elif target>nums[(len(nums))-1]:
            return len(nums)
        m=len(nums)//2
       
        if nums[m]==target:
            return m
        elif nums[m]>target:
            
            while True:
                if nums[m-1]==target:
                    return m-1
                elif nums[m-1]<target:
                    return m
                m-=1
        else:
           
            while True:
                if nums[m+1]==target or  nums[m+1]>target:
                    return m+1
                m+=1


        
