class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        val=0
        jewel=Counter(jewels)
        stones=Counter(stones) 
        for i in jewel:
            val+=stones[i]
        return val       