class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:          # \U0001f527 move check to the top
            return 0

        nums.sort()
        print(nums)

        i = 1                      # current streak length
        k = 1                      # \U0001f527 longest streak found (should start at 1, not 0)
        n = 0

        while n < len(nums) - 1:
            if nums[n] == nums[n+1] - 1:    # consecutive
                i += 1
                k = max(k, i)               # \U0001f527 update longest streak
                n += 1
            elif nums[n] == nums[n+1]:      # duplicate → skip
                n += 1
            else:                           # break in sequence
                i = 1                       # \U0001f527 reset streak counter
                n += 1

        return k                            # \U0001f527 return k (the longest streak)
