class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        val=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and (i*j)%k==0:
                    val+=1
        return val
        