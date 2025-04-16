class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lists=list(s.split())
        return len(lists[-1])
        