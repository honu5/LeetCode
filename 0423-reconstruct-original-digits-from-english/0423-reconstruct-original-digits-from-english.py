class Solution:
    def originalDigits(self, s: str) -> str:
        cnt=Counter(s)
        res=""
        while cnt["z"]>=1 and cnt["e"]>=1 and cnt["r"]>=1 and cnt["o"]>=1:
            res+="0"
            cnt["z"]-=1
            cnt["e"]-=1
            cnt["r"]-=1
            cnt["o"]-=1

        while cnt["t"] >= 1 and cnt["w"] >= 1 and cnt["o"] >= 1:
            res += "2"
            cnt["t"] -= 1
            cnt["w"] -= 1
            cnt["o"] -= 1

        while cnt["f"] >= 1 and cnt["o"] >= 1 and cnt["u"] >= 1 and cnt["r"] >= 1:
            res += "4"
            cnt["f"] -= 1
            cnt["o"] -= 1
            cnt["u"] -= 1
            cnt["r"] -= 1

        while cnt["s"] >= 1 and cnt["i"] >= 1 and cnt["x"] >= 1:
            res += "6"
            cnt["s"] -= 1
            cnt["i"] -= 1
            cnt["x"] -= 1

        while cnt["e"] >= 1 and cnt["i"] >= 1 and cnt["g"] >= 1 and cnt["h"] >= 1 and cnt["t"] >= 1:
            res += "8"
            cnt["e"] -= 1
            cnt["i"] -= 1
            cnt["g"] -= 1
            cnt["h"] -= 1
            cnt["t"] -= 1

        while cnt["t"] >= 1 and cnt["h"] >= 1 and cnt["r"] >= 1 and cnt["e"] >= 2:
            res += "3"
            cnt["t"] -= 1
            cnt["h"] -= 1
            cnt["r"] -= 1
            cnt["e"] -= 2

        while cnt["f"] >= 1 and cnt["i"] >= 1 and cnt["v"] >= 1 and cnt["e"] >= 1:
            res += "5"
            cnt["f"] -= 1
            cnt["i"] -= 1
            cnt["v"] -= 1
            cnt["e"] -= 1

        while cnt["s"] >= 1 and cnt["e"] >= 2 and cnt["v"] >= 1 and cnt["n"] >= 1:
            res += "7"
            cnt["s"] -= 1
            cnt["e"] -= 2
            cnt["v"] -= 1
            cnt["n"] -= 1

        while cnt["o"] >= 1 and cnt["n"] >= 1 and cnt["e"] >= 1:
            res += "1"
            cnt["o"] -= 1
            cnt["n"] -= 1
            cnt["e"] -= 1

        while cnt["n"] >= 2 and cnt["i"] >= 1 and cnt["e"] >= 1:
            res += "9"
            cnt["n"] -= 2
            cnt["i"] -= 1
            cnt["e"] -= 1

        return "".join(sorted(res))
            
        

        
        