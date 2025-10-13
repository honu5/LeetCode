class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        nums.sort(key=len)
        ans=[]
        if len(nums)==1:
            return sorted(nums[0])
        for i in nums[0]:
            count=0
            
            for j in range(1,len(nums)):
                
                if i in nums[j]:
                    
                    count+=1
                if count==len(nums)-1:
                    ans.append(i)

        
        return sorted(ans)
        
        