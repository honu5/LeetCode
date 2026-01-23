class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=Counter(nums)
        i=0
        while i<len(nums):
            if count[nums[i]]!=2:
                nums.pop(i)
            else:
                i+=1
        print(nums)
        return  list(set(nums))
        