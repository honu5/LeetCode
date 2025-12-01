class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n=len(nums)
        longest=0

        for i in range(n):
            
            if nums[i]%2==0 and nums[i]<=threshold:
                right=i+1
                while right<n and nums[right]<=threshold and nums[right]%2!=nums[right-1]%2:
                    right+=1
                current=right-i
                print(current)
                longest=max(current,longest)
        return longest