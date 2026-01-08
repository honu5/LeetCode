class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums1:
            if (i in nums2 or i in nums3) and i not in ans:
                ans.append(i)
        for i in nums2:
            if i in nums3 and i not in ans:
                ans.append(i)
        return ans
        