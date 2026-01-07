class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val=0
        count=Counter(nums)
        for num,frq in count.items():
            if frq==1:
                val+=num
        return val
        