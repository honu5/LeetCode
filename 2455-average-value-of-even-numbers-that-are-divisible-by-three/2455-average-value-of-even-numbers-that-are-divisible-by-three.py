class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        for i in nums:
            if i%6==0:
                ans.append(i)
        if not ans:
            return 0
        return sum(ans)//len(ans)
        