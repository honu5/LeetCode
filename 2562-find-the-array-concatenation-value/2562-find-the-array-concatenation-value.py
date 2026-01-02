class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        summ=0
        while l<=r:
            if l==r:
                summ+=nums[l]
                break
            strs=str(nums[l])+str(nums[r])
            summ+=int(strs)
            l+=1
            r-=1
        
        return summ
