class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=Counter(nums)
                
        for num,freq in c.items():
            if freq==1:
                return num

        
        