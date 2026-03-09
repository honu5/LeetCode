class Solution:
    def simplifyPath(self, path: str) -> str:
        arr=path.split("/")
        ans=[]
        print(arr)
        for i in arr:
            if i=="":
                continue
            elif i==".":
                continue
            elif i=="..":
                if not ans:
                    continue
                else:
                    ans.pop()
            else: ans.append(i)

        
        return "/"+ "/".join(ans)
        
        