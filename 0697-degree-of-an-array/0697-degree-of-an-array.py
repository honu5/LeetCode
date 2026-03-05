class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count=Counter(nums)
        most=count.most_common()
        num=most[0][0]
        val=len(nums)-nums[::-1].index(num)-nums.index(num)
        for i in range(1,len(most)):
            if most[i][1]==most[0][1]:
                y=most[i][0]
                x=len(nums)-nums[::-1].index(y)-nums.index(y)
                val=min(val,x)
            else:
                break
        return val
        