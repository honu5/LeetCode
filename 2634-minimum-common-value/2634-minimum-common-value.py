class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
      
        l=0
        r=0

        while l<len(nums1) and r<len(nums2):
            if nums1[l]==nums2[r]:
                return nums1[l]
            elif nums1[l]>nums2[r]:
                r+=1
            else:
                l+=1
        return -1
        