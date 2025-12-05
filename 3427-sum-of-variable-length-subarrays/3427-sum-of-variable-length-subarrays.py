class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals=0
        acc=0
        prefix_sum=[0]        
        for i in range(len(nums)):
            
            acc+=nums[i]
            prefix_sum.append(acc)
            
        
        
        print(prefix_sum,nums)
        for idx,num in enumerate(nums):
            print(idx)
            size=max(0,idx-num)
            val=prefix_sum[idx+1]-prefix_sum[size]
            vals+=val
        return vals

        