class Solution:
    def maxDifference(self, s: str) -> int:
        count=Counter(s)
        odd=[i for i in count.values() if i%2==0]
        even=[i for i in count.values() if i%2==1]
        return (max(even)-min(odd))
        