class Solution:
    def shortestCompletingWord(self, LP: str, words: List[str]) -> str:
        lp=""
        ans=[]
        for i in LP:
            if  i.isalpha():
                lp+=i.lower()
        count=Counter(lp)
        for i in words:
            isIt=True
            count2=Counter(i)
            for j in count:
                if j not in count2 or  count[j]>count2[j]:
                    isIt=False
                    break
            if isIt: ans.append(i)
        lngth=float("inf")
        for i in ans:
            if len(i)<lngth:
                final_ans=i
                lngth=len(i)
        return final_ans
                



        