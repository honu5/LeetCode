class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        count=Counter(nums)
        most=count.most_common()
        i=0
        val=0
        
        while   i<len(most) and most[i][1]==most[0][1]:
            val+=most[i][1]
            i+=1
        return val
        