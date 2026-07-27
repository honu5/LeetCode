class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sub=[]
        res=[]
        nums.sort()
        def test(i):
            if i==len(nums):
                res.append(sub[:])
                return
            sub.append(nums[i])
            test(i+1)
            sub.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            test(i+1)
        test(0)
        return res
        