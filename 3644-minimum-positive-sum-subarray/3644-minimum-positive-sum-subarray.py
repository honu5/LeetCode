class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        negative=True

        val=float("inf")
        for i in range(l,r+1):
            for a in range(0,len(nums)):
                if a + i > len(nums):      # avoid going out of range
                    break
                if sum(nums[a:a+i])<=0:
                    
                    continue
                
                val=min(val,sum(nums[a:a+i]))
                print(val)
                negative=False
        if negative:
            return -1
    
        return val if val>0 else -1


        