class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        max_length=0
        bound=lcm(*nums)*max(nums)
        for i in range(n):
            curr_gcd=0
            curr_lcm=1
            curr_prod=1
            for j in range(i,n):
                curr_prod*=nums[j]
                if curr_prod>bound:
                    break
                curr_lcm=lcm(curr_lcm,nums[j])
                curr_gcd=gcd(curr_gcd,nums[j])
                if curr_lcm*curr_gcd==curr_prod:
                    max_length=max(max_length,j-i+1)
        return max_length

        
        