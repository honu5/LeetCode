class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        print(nums)
        if len(nums)==1 or nums[0]+nums[1]>=target:
            return 0
        if nums[-1]+nums[0]<target:
            val=len(nums)-1
        else:
        
            for i in range(1,len(nums)):
                
                if nums[i]+nums[0]>=target:
                    val=i-1
                    break
        i=0
        ans=0
        while i<val:
            if nums[val]+nums[i]<target:
                ans+=(val-i)
                i+=1
            else:
                val-=1
        return ans
        