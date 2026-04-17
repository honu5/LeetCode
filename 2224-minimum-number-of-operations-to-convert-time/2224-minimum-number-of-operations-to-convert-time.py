class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hour1=int(current[0:2])
        hour2=int(correct[0:2])
        min1,min2=int(current[3:]),int(correct[3:])
        hr_diff=hour2-hour1
        min_diff=min2-min1
        final=((hr_diff)*60)+min_diff
        ans=0
        
        ans+=final//60
        final=final%60
        ans+=final//15
        final=final%15
        ans+=final//5
        final=final%5
        ans+=final
        return ans
        
