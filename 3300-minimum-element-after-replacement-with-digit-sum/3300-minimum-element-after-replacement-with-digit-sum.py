class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=[]
        for i in range(len(nums)):
            val=0
            for j in str(nums[i]):
                val+=int(j)
            ans.append(val)
        return min(ans)
        