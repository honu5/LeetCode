class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val=0
        count=Counter(nums)
        for frq,num in count.items():
            print(frq,num)
            if num>1:
                val+=((num-1)*(num))/2
        return val

        