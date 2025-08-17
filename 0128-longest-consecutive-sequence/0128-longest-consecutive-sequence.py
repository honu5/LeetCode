class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 1
        nums.sort()
        i=1
        n=0
        k=0
        if len(nums)==0:
            return 0
        print(nums)
        streak=0
        while n<len(nums)-1:

            if nums[n]==nums[n+1]-1:
                i+=1
                n+=1
                
            elif nums[n]==nums[n+1]:
                n+=1
            else:
                i=1
                n+=1
            streak=max(i,streak)
            

            
        return streak


        