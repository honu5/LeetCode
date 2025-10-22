class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=len(set(nums))
        i=0
        while i<k-1:
            if nums[i]==nums[i+1]:
                nums.pop(i)
            else:
                i+=1
        return k

        