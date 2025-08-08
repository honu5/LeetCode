class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=Counter(nums)
        for i in count:
            if count[i]>1:
                return True
        return False
        
        