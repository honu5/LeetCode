class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        summ=0
        while l<r:
            strs=str(nums[l])+str(nums[r])
            summ+=int(strs)
            l+=1
            r-=1
            print(summ)
        if len(nums)%2==1:
            summ+=nums[len(nums)//2]
        return summ
