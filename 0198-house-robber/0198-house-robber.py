class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1=prev2=0
        for i in nums:
            curr=max(prev1,prev2+i)
            prev2=prev1
            prev1=curr
        return curr
        