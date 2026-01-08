class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        val1=[]
        val2=[]
        for i in nums1:
            if i not in nums2 and i not in val1:
                val1.append(i)
        for i in nums2:
            if i not in  nums1 and i not in val2:
                val2.append(i)
        return [val1,val2]
        