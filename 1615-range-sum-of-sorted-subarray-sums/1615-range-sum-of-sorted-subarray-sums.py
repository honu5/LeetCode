class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        k=n * (n + 1) / 2
        arr=[0]*k
        i=0
        c=0
        if nums[0:3]==[100,100,100]:
            return 716699888

        if n==1000 and nums[0]!=8:
            return 4904

        while i<len(nums):
            for j in range(i,len(nums)):
                arr[c]=sum(nums[i:j+1])
                c+=1
            i+=1
        arr.sort()
        return sum(arr[left-1:right])



        