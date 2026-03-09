class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count=Counter(nums)
        most=count.most_common()
        if most[0][1]>2:
            return False
        val=0
        for i in count.values():
            val+=i
        return val%2==0
        