class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val=0
        n=len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                for k in range(j+1,n-1):
                    for l in range(k+1,n):
                        if nums[i]+nums[j]+nums[k]==nums[l]:
                            val+=1
        return val

        