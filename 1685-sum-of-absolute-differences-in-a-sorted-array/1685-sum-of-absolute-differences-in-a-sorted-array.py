class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''f,s=0,0
        n=len(nums)
        idx=0
        res=[]
        while (s<n):
            idx+=abs(nums[s]-nums[f])
            f+=1
            if f==n:
                s+=1
                res.append(idx)
                idx=0
                f=0
        return res'''
        '''cumm=sum(nums)
        res=[]
        for i in nums:
            idx=0
            for j in range(len(nums)):
                idx+=abs(i-nums[j])
            res.append(idx)
        return res'''

        n = len(nums)
        res = []

        prefix_sum=[0]*(n+1)
        for i in range(n):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]
        total_sum=prefix_sum[n]

        for i in range(n):
            idx=0
            left_sum=prefix_sum[i]
            right_sum=total_sum-prefix_sum[i]
            m=n-i
            idx+=right_sum-(m*nums[i])+abs(left_sum-(i*nums[i]))
            res.append(idx)
        return res
