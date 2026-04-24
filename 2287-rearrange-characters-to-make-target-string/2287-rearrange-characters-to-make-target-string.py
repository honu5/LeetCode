class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count=Counter(s)
        return min(count[i]//counts for i,counts in Counter(target).items())

        