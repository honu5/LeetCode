class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val=0
        if 0 in nums:
            return 0
        for i in nums:
            if i<0:
                val+=1
        if val%2==1:
            return -1
        return 1
        