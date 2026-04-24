class Solution:
    def maxSum(self, nums: List[int]) -> int:
        _dict={}
        
        for i in nums:
            l=max(list(map(int, str(i))))
            if l in _dict.keys():
                _dict[l].append(i)
            else: _dict[l]=[i]
        ans=0
        for i,frq in _dict.items():
            if len(frq)<2:
                continue
            frq.sort()
            ans=max(frq[-1]+frq[-2],ans)
        return ans if ans else -1
            
        