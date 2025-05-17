class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
        '''low=0
        mid=0
        high=0
        pivot=1
        while mid<high:
            if nums[mid]<pivot:
                nums[mid],nums[low]='''
        
        