class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans=[]
        
        for i in ops:
            
            
            if i.isdigit() :
                ans.append(int(i))
            
            elif i=="C" :
               ans.pop()
                
            elif i=="D":
                ans.append(2*ans[-1])
           
           
           
            elif i=="+":
                ans.append(ans[-1]+ans[-2])
            else: ans.append(int(i))
            print(ans)    
        return sum(ans)
            