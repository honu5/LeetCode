class Solution:
    def reverseVowels(self, s: str) -> str:
        Vowels=['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
        S=list(s)
        l=0
        r=len(S)-1
        while l<r:
            if S[l] in Vowels:
                if S[r] in Vowels:
                    S[l],S[r]=S[r],S[l]
                    l+=1
                    r-=1
                else: r-=1
            else:l+=1
        S="".join(S)
        return S
            

            

