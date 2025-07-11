class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=Counter(nums)
        d=c.most_common()[-1]
        print(d)
        return d[0]

        
        