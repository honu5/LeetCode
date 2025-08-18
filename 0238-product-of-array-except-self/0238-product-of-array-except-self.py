class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''ans=[]
        product=reduce(operator.mul,nums,1)
        for i in range(len(nums)-1):
            val=nums[i]
            nums.remove(val)
            print(nums)
            ans.append(reduce(operator.mul,nums,1))
            print(nums,reduce(operator.mul,nums,1))
            nums.insert(i,val)
            
           
           
        print(nums)
        ans.append(reduce(operator.mul,nums[0:len(nums)-1],1))
        
        return ans'''

        n=len(nums)
        ans=[1]*n
        prefix=1
        for i in range(n):
            ans[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(n-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans