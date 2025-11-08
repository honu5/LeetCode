class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        l=0
        r=len(nums)-1
        ans=[]
        while l<=r:
            avr=(nums[l]+nums[r])/2.0
            ans.append(avr)
            l+=1
            r-=1
        return min(ans)

        