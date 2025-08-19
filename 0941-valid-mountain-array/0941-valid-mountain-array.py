class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        flag="up"
        if arr==sorted(arr) or arr==list(reversed(sorted(arr))):
            return False
        nums=arr
        if len(arr)<3:
            return False
        for i in range(len(arr)-1):
            if nums[i]>nums[i+1]:
                flag="down"
            elif nums[i]==nums[i+1]:
                return False
            if flag=="down" and nums[i]<nums[i+1]:
                return False
        return True
            
        