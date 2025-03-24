class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        a=set()
        for start,end in meetings:
            for day in range(start,end+1):
                a.add(day)
        return days - len(a)
