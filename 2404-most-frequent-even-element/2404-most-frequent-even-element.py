class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=-1
        found=False
        for i in nums:
            if i%2==0:
                found=True
        if not found:
            return -1
        val=float("inf")
        count=Counter(nums)
        most=count.most_common()
        mosts=most[0][1]
        for i,frq in count.items():
            print(i,frq,m,val)
            if i%2==0 and (frq>m or (frq==m and i<val)):
                val=i
                m=frq
        
        return val

        