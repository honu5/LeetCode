class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if k>len(nums):
            k=k%len(nums)
        '''while k:
            popped=nums.pop()
            nums.insert(0,popped)
            k-=1'''

        nums[0:0]=nums[n-k:]
        nums[n:]=[]