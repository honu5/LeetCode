class Solution:
    def minimumMoves(self, s: str) -> int:
        if not 'X' in s:
            return 0
        n=len(s)
        val=0
        i=0
        while i<n:
            if s[i]=='X':
                val+=1
                i+=3
            else: i+=1

        return val