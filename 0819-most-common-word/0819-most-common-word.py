class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        x=""
        for i in paragraph:
            if i.isalpha() or i==" ":
                x+=i
            else : x+=" "
        y=x.split()
        for i in range(len(y)):
            y[i]=y[i].lower()
        print(y)
        count=Counter(y)
        most=count.most_common()
        for i in range(len(most)):
            if most[i][0] in banned:
                continue
            return most[i][0]
            

                
        

        