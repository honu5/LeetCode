class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=Counter(s)
        most=count.most_common()
        return most[0][1]==most[-1][1]