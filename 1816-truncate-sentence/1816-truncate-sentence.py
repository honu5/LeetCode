class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        num=s.split()
        nums=num[:k]
        t=""
        for i in range(len(nums)-1):
            t+=nums[i]
            t+=" "
        t+=nums[-1]
        return t
        