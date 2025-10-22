class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)==2:
            return 1
        
        l=0
        r=len(nums)-1
        arr=[]
        while l<r:
            average=nums[l]+nums[r]
            if average not in arr:
                arr.append(average)
            l+=1
            r-=1
        return len(arr)

        