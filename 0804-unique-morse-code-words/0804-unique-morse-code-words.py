class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        val=0
        alph=0
        _dict={}
        lst=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        while alph<26:
            _dict[chr(97+alph)]=lst[val]
            val+=1
            alph+=1
        ans=[]
        for i in words:
            string=""
            for j in i:
                string+=_dict[j]
            ans.append(string)
        return len(set(ans))
        