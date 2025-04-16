class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lists=list(s.split())
        n=len(lists)
        return len(lists[n-1])
        