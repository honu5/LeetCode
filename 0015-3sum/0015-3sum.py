class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        c=[]
        nums.sort()
        
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            if i!=0 and  nums[i]==nums[i-1]:
                continue
            while left<right:
                d=nums[i] + nums[left] + nums[right]
                if d==0:
                    c.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1

                    if left<right and nums[right] == nums[right+1]:
                        right-=1
                   
                elif d<0:
                    left+=1
                else: right-=1
        return c




            