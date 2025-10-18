class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        n=len(nums)
        while i<n:
            if nums[i]==0:
                nums.pop(i)
                n-=1
                i-=1
            i+=1
        print(nums)
        return len(set(nums))
        