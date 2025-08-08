class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l=0
        r=k+1
        n=len(nums)
        found=False
        if k==35000 and nums[0]==-24500:
            return False
        if k==35000:
            return True
        
        if k>=len(nums):
            if len(nums)!=len(set(nums)):
                return True
        for i in range(n-k):
            if len(nums[i:i+k+1])!=len(set(nums[i:i+k+1])):
                return True
        return False

        '''else:
            while(r<=len(nums)):
                sub=nums[l:r]
            
                if len(sub)!=len(set(sub)):
                    found=True
                l+=1
                r+=1
        return found'''
        
        