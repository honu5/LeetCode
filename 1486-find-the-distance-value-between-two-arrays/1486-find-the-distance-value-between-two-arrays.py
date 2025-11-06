class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        l=0
        val=0
        while l<len(arr1):
            found=True
            for i in arr2:
                if abs(arr1[l]-i)<=d:
                    found=False
                    break
            if found:
                val+=1
            l+=1
        return val
        