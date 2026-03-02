class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val=0
            for j in str(nums[i]):
                val+=int(j)
            if i==val:
                return val
        return -1
        