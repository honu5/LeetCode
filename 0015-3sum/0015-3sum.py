class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i==0 or i>0 and  nums[i]!=nums[i-1]:
                l,r=i+1,len(nums)-1
                while l<r:
                    c=nums[i]+nums[l]+nums[r]
                    if c==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif c<0:
                        l+=1
                    else: r-=1
        return res

                        
