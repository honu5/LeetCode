class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)
        valid=0
        left_sum=0
        for i in nums:
            if i!=0:
                left_sum+=i
            else:
                if left_sum*2==total:
                    valid+=2
                elif abs((left_sum*2)-total)==1:
                    valid+=1
        return valid
            
        