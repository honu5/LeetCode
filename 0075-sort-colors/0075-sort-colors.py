class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0 # 0
        mid = 0 # 1
        high = len(nums) - 1 # 2

        pivot = 1

        while mid <= high:
            if nums[mid] < pivot: # 0
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] > pivot:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            else: # it is the pivot
                mid += 1
        return nums