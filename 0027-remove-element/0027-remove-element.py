class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        
        i=0 
        while (i<n):
            if nums[i]==val:
                elem=nums.pop(i)
                nums.append(elem)
                n-=1
            else:
                i+=1
        return n
        
        