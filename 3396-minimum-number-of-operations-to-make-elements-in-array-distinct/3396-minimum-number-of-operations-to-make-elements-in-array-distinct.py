class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums)==len(set(nums)):
            return 0
        
        nums=nums[::-1]
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] in nums[:i]:
                ans=len(nums[i:])
                print(ans)
                break
        return (ans//3)+1 if ans%3!=0 else ans//3


        