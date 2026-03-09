class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels=['a', 'e', 'i', 'o', 'u']
        count=Counter(s)
        most=count.most_common()
        val=most[0][1]
        if most[0][0] in vowels:
            for i in range(len(most)):
                if most[i][0] not in vowels:
                    return val+most[i][1]
        else:
            for i in range(len(most)):
                if most[i][0]  in vowels:
                    return val+most[i][1]
        return val


        