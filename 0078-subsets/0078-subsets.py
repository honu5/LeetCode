class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        def test(i):
            if i==len(nums):
                res.append(sub[:])
                return 
            sub.append(nums[i])
            test(i+1)
            sub.pop()
            test(i+1)
        test(0)
        return res