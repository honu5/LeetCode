class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)//3
        ans=[]
        counter=Counter(nums)
        for i,frq in counter.items():
            if frq>n:
                ans.append(i)
        return ans
        