class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)
        if len(a)!=len(nums):
            return True
        return False
        