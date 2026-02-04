class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val=0
        for i in nums:
            if len(str(i))>1:
                for j in str(i):
                    val+=int(j)
            else:
                val+=i
        return abs(val-sum(nums))

        