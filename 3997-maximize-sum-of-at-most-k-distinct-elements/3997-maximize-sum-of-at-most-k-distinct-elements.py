class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        a=list(set(nums))
        a.sort()
        if len(a)-k>0 :
            n=len(a)-k 
        else: n=0
        return sorted((a[n:]),reverse=True)    