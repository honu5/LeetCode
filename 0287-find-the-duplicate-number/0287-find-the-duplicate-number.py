class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=Counter(nums)
        c=count.most_common()
        return c[0][0]
        