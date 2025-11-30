class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums)==1:
            return str(nums[0])
        nums=[str(i) for i in nums]
        def comp(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                0
        nums.sort(key=cmp_to_key(comp))
        if nums[0]=="0":
            return "0"
        return "".join(nums)
