class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count=Counter(s)
        count1=Counter(target)
        val=float("inf")
        for i in count1:
            val=min(val,count[i]//count1[i])
        return val
        

        