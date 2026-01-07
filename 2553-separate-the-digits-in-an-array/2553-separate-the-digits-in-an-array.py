class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums:
            if len(str(i))>1:
                for j in str(i):
                    ans.append(int(j))
            else:
                ans.append(i)
        return ans
        