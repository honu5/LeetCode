class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        if n==0 or (n==1 and nums[0]==val):
            return 0
        elif n==1 and nums[0]!=val:
            return 1
        i=0 
        while (i<n):
            if nums[i]==val:
                elem=nums.pop(i)
                nums.append(elem)
                n-=1
            else:
                i+=1
        return n
        
        