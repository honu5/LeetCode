class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        a=list(set(nums))
        a.sort()
        n=len(a)
        return sorted((a[max((n-k),0):]),reverse=True)    