class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0,-1*(pow(2,32)))
        nums.append(-1*(pow(2,32)))
        print(nums)
        for i in range(1,len(nums)-1):
            print("a")
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                return i-1
        
        