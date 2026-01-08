class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''if sum(num)%2==1:
            return False
        half=sum(nums)/2'''
        count=Counter(nums)
        for i,frq in count.items():
            if frq%2==1:
                return False
        return True

        