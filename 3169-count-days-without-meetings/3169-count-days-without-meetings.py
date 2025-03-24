class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        a=sorted(meetings)
        ans=last=0
        for start , end in a:
            if last<start:
                ans+=start-last-1
            last=max(last,end)
        ans+=days-last
        return ans
        