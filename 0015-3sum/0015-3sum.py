class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i in range(len(nums)):
            

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0 and  [nums[i],nums[left],nums[right]] not in res:
                    res.append([nums[i], nums[left], nums[right]])

                    

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
