class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=Counter(s)
        ans=[i for i in count.values()]
        if len(set(ans))!=1:
            return False
        return True
        