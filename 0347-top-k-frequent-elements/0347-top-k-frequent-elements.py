class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        counter=Counter(nums)
        mf=counter.most_common()
        for i in range(k):
            ans.append(mf[i][0])
        return ans
        