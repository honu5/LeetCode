class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l=0
        r=len(nums)-1
        cnt=0
        nums.sort()
        while l<r:
            summ=nums[l]+nums[r]

            if summ ==k:
                cnt+=1
                l+=1
                r-=1
            elif summ<k:
                l+=1
            else: r-=1
        return cnt
        